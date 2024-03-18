import os
import grpc
from concurrent import futures
import logging
import random 
# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import generated gRPC code
import image_search_pb2_grpc as image_search_pb2_grpc
import image_search_pb2 as image_search_pb2

class ImageSearchServicer(image_search_pb2_grpc.ImageSearchServicer):
    def SearchImage(self, request, context):
        keyword = request.keyword
        logger.info(f"Received search request for keyword: {keyword}")
        image_data = self.fetch_image_from_database(keyword)
        return image_search_pb2.ImageResponse(image_data=image_data)

    def Ping(self, request, context):
        logger.info("Received Ping request")
        return image_search_pb2.PingResponse(message="Pong")

    def fetch_image_from_database(self, keyword):
        # Logic to fetch image from the database
        keyword = keyword.lower()
        image_path = os.path.join('/app/images', keyword)
        logger.info(f"Checking existence of directory: {image_path}")
        if os.path.isdir(image_path):
            logger.info(f"Directory {image_path} exists.")
            image_files = [f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))]
            logger.info(f"Found image files in directory: {image_files}")
            if image_files:
                random_image = random.choice(image_files)
                full_path = os.path.join(image_path, random_image)
                with open(full_path, 'rb') as image_file:
                    return image_file.read()
            else:
                logger.warning(f"No image files found in directory: {image_path}")
                return b''  # Return empty bytes if no image files found
        else:
            logger.warning(f"Directory {image_path} does not exist or is not a directory.")
            return b''  # Return empty bytes if directory does not exist or is not a directory


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_search_pb2_grpc.add_ImageSearchServicer_to_server(ImageSearchServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.info("Server started. Listening on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
