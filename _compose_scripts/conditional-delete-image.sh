#!/bin/bash

# Check if an image name argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <image_name>"
    exit 1
fi

IMAGE_NAME="$1"

# Escape special characters in the image name using printf
ESCAPED_NAME=$(printf "%q" "$IMAGE_NAME")

# Check if the image exists
if docker image inspect "$ESCAPED_NAME" &> /dev/null; then
    # Remove the image if it exists
    printf "Deleting image ${ESCAPED_NAME}...\n"
    docker rmi "$ESCAPED_NAME"
else
    # Image does not exist, no action needed
    printf "Image ${ESCAPED_NAME} does not exist. No action needed.\n"
fi