import grpc
import server.image_search_pb2 as image_search_pb2
import server.image_search_pb2_grpc as image_search_pb2_grpc
import logging
import sys

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run(keyword):
    # Establish a connection to the gRPC server
    logger.info("Connecting to gRPC server...")
    # Use the IP address of the server container (172.17.0.2 in this case)
    server_address = '172.17.0.2:50051'
    channel = grpc.insecure_channel(server_address)

    # Create a stub (client) for the ImageSearch service
    stub = image_search_pb2_grpc.ImageSearchStub(channel)

    # Create a request message
    request = image_search_pb2.SearchRequest(keyword=keyword)

    # Call the SearchImage RPC with the request and get the response
    response = stub.SearchImage(request)

    # Check if the received image data is empty
    if not response.image_data:
        raise RuntimeError("Received empty image data or no image found")

    # Save the received image data to a file
    image_file_path = f"{keyword}.jpg"
    with open(image_file_path, 'wb') as image_file:
        image_file.write(response.image_data)

    logger.info(f"Received image data and saved to {image_file_path}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python client.py <keyword>")
        sys.exit(1)

    keyword = sys.argv[1]
    run(keyword)
