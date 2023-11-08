# README #

This README will document every steps that are necessary to get the Python application up and running.

# Python "Hello, World!" Application with Docker and Minikube Load Balancing

This project demonstrates how to create a simple "Hello, World!" application in Python, build it within a Docker container, and load balance the application within Minikube.

## Getting Started

Step 1: Create a Python "Hello, World!" Application

Create a directory for your project and navigate into it:
mkdir hello-world-python
cd hello-world-python

Create a Python script app.py, this script uses the Flask web framework to create a simple "Hello, World!" web application.

Step 2: Create a Dockerfile
In the same directory, create a Dockerfile (Dockerfile) to build a Docker image for the Python application.

This Dockerfile sets up a Python environment, installs Flask, exposes port 80, and runs your Python script.

Step 3: Build the Docker Image
In the same directory, build the Docker image using the command:

docker build -t hello-world-python .

Step 4: Run the Application in Docker
Run the Docker container:

docker run -d -p 8080:80 hello-world-python

This command starts the container in detached mode (-d) and maps port 8080 on your host to port 80 in the container. The Flask app will be accessible at http://localhost:8080.

Step 5: Install and Start Minikube
Follow the official Minikube documentation to install Minikube: Minikube Installation Guide https://minikube.sigs.k8s.io/docs/start/

Start Minikube:

minikube start

Step 6: Deploy the Application to Minikube
Create a Kubernetes Deployment and Service for the Python application:

hello-world-deployment.yaml
hello-world-service.yaml

Apply the deployment and service to Minikube:

kubectl apply -f hello-world-deployment.yaml
kubectl apply -f hello-world-service.yaml

This deploys the application, creates pods, and sets up a LoadBalancer service.

Step 7: Access the Load-Balanced Application
Retrieve the external IP address for the LoadBalancer service:

minikube service hello-world-service

Access the application using the external IP address, and it should be load-balanced across the pods.

### Prerequisites

- Install Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)
- Install Minikube: [Minikube Installation Guide](https://minikube.sigs.k8s.io/docs/start/)

### Build and Run the Python Application

```bash
# Build the Docker image
docker build -t hello-world-python .

# Run the Docker container
docker run -d -p 8080:80 hello-world-python
