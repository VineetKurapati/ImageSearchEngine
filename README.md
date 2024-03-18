# gRPC Image Search

This project implements an image search service using gRPC. It consists of a server that accepts search requests and returns corresponding images, and a client that interacts with the server to perform searches based on keywords.

## Features

- Search for images based on keywords
- Ping the server for connectivity testing

## Requirements

- [Go](https://golang.org/) (for building and running the client)
- [Python](https://www.python.org/) (for running the server)
- [Docker](https://www.docker.com/) (for running the server and client in containers)

## Setup

### Running the Server

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/gRPC-image-search.git
    cd gRPC-image-search
    ```

2. Build the server Docker image:

    ```bash
    docker build -t image-search-server -f Dockerfile_server .
    ```

3. Run the server container:

    ```bash
    docker run -v /ImageSearch/images:/app/images image_search_server
    ```

### Running the Client

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/gRPC-image-search.git
    cd gRPC-image-search
    ```

2. Build the client Docker image:

    ```bash
    docker build -t my-client-image .                                                           
    ```

3. Run the client container:

    ```bash
   docker run my-client-image <keyword>   
    ```

    Replace `[keyword]` with the keyword you want to search for.

## Usage

Once the server and client are running, you can search for images using the client by providing a keyword as a command-line argument. For example:

```bash
docker run -it --rm image-search-client cat
