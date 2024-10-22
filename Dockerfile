FROM python:latest

# Update and install required packages
RUN apt-get update -y && apt-get upgrade -y

# Install additional dependencies
RUN apt-get install -y python3-lib2to3

# Upgrade pip
RUN pip3 install -U pip

# Copy app code to container
COPY . /app/
WORKDIR /app/

# Install Python dependencies
RUN pip3 install -U -r requirements.txt

# Run the application
CMD ["python3", "main.py"]
