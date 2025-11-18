# Base python version (lightweight preferable)
FROM python:3.9-slim

# directory definition to store the code and needed utilities
WORKDIR /app

# we copy app.py within container
COPY src/app.py .

# We define the container initialization
CMD ["python", "app.py"]