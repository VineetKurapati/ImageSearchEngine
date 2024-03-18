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
        if image_data is not None:
            self.save_image_to_server(image_data, keyword)
        # Return the image_data if found, otherwise return None
        return image_search_pb2.ImageResponse(image_data=image_data)

    def save_image_to_server(self, image_data, keyword):
        save_path = "/app/client_images/"  # Adjust the path as needed
        os.makedirs(save_path, exist_ok=True)
        with open(os.path.join(save_path, f"{keyword}.jpg"), 'wb') as image_file:
            image_file.write(image_data)
        logger.info(f"Image Saved in {save_path}")

    def Ping(self, request, context):
        logger.info("Received Ping request")
        return image_search_pb2.PingResponse(message="Pong")

    def fetch_image_from_database(self, keyword):
        keyword = keyword.lower()
        image_path = os.path.join('/app/images', keyword)
        logger.info(f"Checking existence of directory: {image_path}")
        if os.path.isdir(image_path):
            logger.info(f"Directory {image_path} exists.")
            image_files = [f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))]
            if image_files:
                random_image = random.choice(image_files)
                full_path = os.path.join(image_path, random_image)
                with open(full_path, 'rb') as image_file:
                    return image_file.read()
            else:
                logger.warning(f"No image files found in directory: {image_path}")
                return None  # Return None if no image files found
        else:
            logger.warning(f"Directory {image_path} does not exist or is not a directory.")
            return None  # Return None if directory does not exist or is not a directory


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_search_pb2_grpc.add_ImageSearchServicer_to_server(ImageSearchServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.info("Server started. Listening on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
