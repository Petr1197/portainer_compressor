FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src ./src

# Set the environment variables for HandBrakeCLI
ENV HANDBRAKE_PATH=/usr/bin/HandBrakeCLI

# Install HandBrakeCLI
RUN apt-get update && \
    apt-get install -y handbrake-cli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the command to run the application
CMD ["python", "src/main.py"]