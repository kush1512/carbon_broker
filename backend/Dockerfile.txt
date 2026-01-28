# Use an official Python image as a parent image
FROM python:3.10-slim

# Set the working directory for the container to the root
WORKDIR /

# Install system dependencies required for GDAL and other geospatial libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    && rm -rf /var/lib/apt/lists/*

# Create a directory for our application code
RUN mkdir -p /usr/src/app

# Set the Python path to include our app directory
ENV PYTHONPATH="/usr/src/app:${PYTHONPATH}"

# Copy the requirements file into the app directory
COPY ./requirements.txt /usr/src/app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip
# Set CPLUS_INCLUDE_PATH and C_INCLUDE_PATH for GDAL headers
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Copy the application code into the app directory
COPY ./app /usr/src/app/app

# Expose the port the app runs on
EXPOSE 8000