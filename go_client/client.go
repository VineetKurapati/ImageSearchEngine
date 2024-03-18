package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"log"
	"os"

	pb "client.go/generated" // Import generated gRPC code
	"google.golang.org/grpc"
)

func main() {
	// Set up a connection to the server.
	conn, err := grpc.Dial("172.17.0.2:50051", grpc.WithInsecure()) // Assuming server is the hostname of your server container
	if err != nil {
		log.Fatalf("Failed to dial server: %v", err)
	}
	defer conn.Close()

	// Create a client instance of the ImageSearch service
	client := pb.NewImageSearchClient(conn)

	// Call the Ping method
	pingResponse, err := client.Ping(context.Background(), &pb.PingRequest{})
	if err != nil {
		log.Fatalf("Ping call failed: %v", err)
	}

	// Log the response
	log.Printf("Ping response: %s", pingResponse.GetMessage())

	// Get keyword from command-line arguments or input from user
	var keyword string
	if len(os.Args) < 2 {
		fmt.Print("Enter a keyword to search for images: ")
		fmt.Scanln(&keyword)
	} else {
		keyword = os.Args[1]
	}

	// Call the SearchImage method
	imageResponse, err := client.SearchImage(context.Background(), &pb.SearchRequest{Keyword: keyword})
	if err != nil {
		log.Fatalf("SearchImage call failed: %v", err)
	}

	// Handle the response
	imageData := imageResponse.GetImageData()
	if len(imageData) == 0 {
		log.Fatalf("No image found for keyword: %s", keyword)
	} else {
		// Save the image data to a file
		imagePath := "/app/images/" // Adjust the path as needed
		err := ioutil.WriteFile(fmt.Sprintf("%s%s.jpg", imagePath, keyword), imageData, 0644)
		if err != nil {
			log.Fatalf("Failed to save image: %v", err)
		}
		log.Printf("Image saved successfully: %s%s.jpg", imagePath, keyword)
	}
}
