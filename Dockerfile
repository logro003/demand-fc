# Use the official Python 3.11.3 image with slim buster Linux as the base image
FROM python:3.11.3-slim-buster

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libffi-dev \
        libssl-dev \
        curl \
        git \
        && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the dependency file to the working directory
COPY poetry.lock pyproject.toml /app/

# Install Poetry
RUN pip install poetry==1.7.1

# Install project dependencies
RUN poetry install --no-root

# Copy the rest of the application code
COPY . /app/

# Expose the port the application runs on
EXPOSE 8000

# Set up volumes
VOLUME ["/app/output"]

#ENTRYPOINT ["python", "app/main.py"]