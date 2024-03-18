# Use the official Go image as a parent image
FROM golang:latest AS builder

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy go.mod and go.sum files
COPY go.mod go.sum ./

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download

# Copy the source code into the container
COPY . .

# Build the Go app
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o client .

# Start a new stage from scratch
FROM alpine:latest

# Set the Current Working Directory inside the container
WORKDIR /app

# Create the images directory
RUN mkdir -p /app/images

# Copy the Pre-built binary file from the previous stage
COPY --from=builder /app/client .

# Command to run the executable
ENTRYPOINT ["./client"]
