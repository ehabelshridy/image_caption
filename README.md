AI Image Captioning Web App
This project is a localized AI application that uses the BLIP (Bootstrapping Language-Image Pre-training) model to generate descriptive captions for images. It features a user-friendly web interface built with Gradio and is fully containerized using Docker.

Features
Automated Captioning: Generates accurate text descriptions for any uploaded image using Salesforce's BLIP model.

Gradio Interface: A clean, interactive web UI accessible via any browser.

Containerized: Ready to deploy anywhere using Docker.


Optimized for Docker: Uses a slim Python base image to reduce storage footprint.

Tech Stack
Language: Python 3.9

Framework: Gradio

AI Model: Salesforce/blip-image-captioning-base (via Transformers)


Libraries: PyTorch, Pillow, NumPy, Requests.

Deployment: Docker

Prerequisites
Before running the project, ensure you have:

Python 3.9+ installed (for local running).

Docker installed (for containerized running).

How to Run
Option 1: Running Locally
Prepare your environment:

Bash
python -m venv my_env
# Activate on Windows:
.\my_env\Scripts\activate
# Activate on Mac/Linux:
source my_env/bin/activate

Install Dependencies: 

Bash
pip install -r requirements.txt
Start the Application:

Bash
python image_cap.py
Open your browser at http://localhost:7860.

Option 2: Running with Docker
Build the Docker Image:

Bash
docker build -t image-captioning-app .
Run the Container:

Bash
docker run -p 7860:7860 image-captioning-app
Access the app at http://localhost:7860.

Dockerfile Explained
The provided Dockerfile performs the following steps:


Base Image: Uses python:3.9-slim to keep the environment lightweight.


Dependencies: Installs necessary system tools and Python packages without keeping temporary cache files to save space (--no-cache-dir).


Networking: Exposes port 7860 and sets the environment variable GRADIO_SERVER_NAME="0.0.0.0" to allow external access.

File Structure
image_cap.py: The main logic for image processing and the Gradio UI.

Dockerfile: The instructions for building the Docker container.


requirements.txt: List of Python libraries including transformers and torch.

👨‍🏫 Author
Ehab El-Shridy
