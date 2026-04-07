# 1. Use an official Python runtime as a parent image
FROM python:3.9-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Install system dependencies (needed for some image processing libraries)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy the requirements file into the container
COPY requirements.txt .

# 5. Install the required Python packages
# We use --no-cache-dir to keep the image size small
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application code
COPY . .

# 7. Expose the port Gradio uses (default is 7860)
EXPOSE 7860

# 8. Set environment variable to make Gradio accessible outside the container
ENV GRADIO_SERVER_NAME="0.0.0.0"

# 9. Command to run the application
CMD ["python", "image_cap.py"]