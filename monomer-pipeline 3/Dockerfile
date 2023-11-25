# Use the official Python image from Docker Hub
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy local code to the container image
COPY . /app

# Install dependencies
RUN pip install biopython numpy weasyprint

# If you have other dependencies that need to be installed via apt-get, add them here
# RUN apt-get update && apt-get install -y \
#     some-other-dependencies-you-might-need

# Specify the command to run
CMD ["./pipeline.sh"]
