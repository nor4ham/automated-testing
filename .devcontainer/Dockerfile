# Use the official Python image
FROM python:3.8-slim

# Install dependencies (Selenium, Pytest, Appium, etc.)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium-driver \
    gnupg \
    apt-transport-https \
    ca-certificates \
    && apt-get clean

#  Install Chrome and Chromedriver in Your Dockerfile (if you want to control everything)

# Install Python packages
RUN pip install selenium pytest appium-python-client

# Set the working directory
WORKDIR /workspace

# Copy the project files into the container
COPY . /workspace
