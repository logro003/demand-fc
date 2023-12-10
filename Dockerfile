# Use the official Python 3.11.3 image with slim buster Linux as the base image
FROM python:3.11.3-slim-buster

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libffi-dev \
        libssl-dev 

# Set the working directory in the container
WORKDIR /demand_forecast

# Copy the application code
COPY . /demand_forecast/

# Install Poetry
RUN pip install poetry==1.7.1

# Install project dependencies
RUN poetry install --no-root

# Setting python path to root folder 
ENV PYTHONPATH /demand_forecast

# Expose the port the application runs on - in caSe of rest API 
#EXPOSE 8000

# Set up volumes
VOLUME ["/demand_forecast/output", "/demand_forecast/input"]

# Set the container’s primary purpose - running the model training and prediction
ENTRYPOINT ["poetry", "run", "python",  "app/main.py"]