# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /consumer

# Copy the current directory contents into the container at /consumer
COPY . /consumer

# Install any needed packages specified in requirements.txt
RUN pip install kafka-python elasticsearch redis

# Run consumer.py when the container launches
CMD ["python", "consumer.py"]
