package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strings"

	pb "client.go/generated"
	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("172.17.0.2:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to dial server: %v", err)
	}
	defer conn.Close()

	client := pb.NewImageSearchClient(conn)

	// Call the Ping method
	pingResponse, err := client.Ping(context.Background(), &pb.PingRequest{})
	if err != nil {
		log.Fatalf("Ping call failed: %v", err)
	}
	log.Printf("Ping response: %s", pingResponse.GetMessage())

	// Get keywords from command-line arguments or from input list
	var keywords []string
	if len(os.Args) > 1 {
		// If keywords are provided as command-line arguments
		keywords = os.Args[1:]
	} else {
		// If no command-line arguments are provided, read keywords from input list
		fmt.Println("Enter keywords separated by spaces:")
		var input string
		fmt.Scanln(&input)
		keywords = parseInputList(input)
	}

	// Call the SearchImage method for each keyword
	for _, keyword := range keywords {
		imageResponse, err := client.SearchImage(context.Background(), &pb.SearchRequest{Keyword: keyword})
		if err != nil {
			log.Fatalf("SearchImage call failed for keyword %s: %v", keyword, err)
		}

		imageData := imageResponse.GetImageData()
		if len(imageData) == 0 {
			log.Printf("No image found for keyword: %s", keyword)
		} else {
			// Save the image data to a file
			savePath := fmt.Sprintf("/app/images/%s.jpg", keyword)
			err := ioutil.WriteFile(savePath, imageData, 0644)
			if err != nil {
				log.Fatalf("Failed to save image for keyword %s: %v", keyword, err)
			}
			log.Printf("Image saved successfully for keyword %s:", keyword)
		}
	}
}

// Function to parse input list of keywords separated by spaces
func parseInputList(input string) []string {
	var keywords []string
	for _, word := range strings.Fields(input) {
		keywords = append(keywords, word)
	}
	return keywords
}
