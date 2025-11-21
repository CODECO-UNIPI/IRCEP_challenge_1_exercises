# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY src/counter.py .

# Run the Python script when the container starts
CMD ["python", "counter.py"]
