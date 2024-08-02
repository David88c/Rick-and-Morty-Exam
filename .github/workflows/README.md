# CI/CD Pipeline for Rick and Morty Application

This repository contains the CI/CD pipeline configuration for building, pushing, and deploying the Rick and Morty application using GitHub Actions. The pipeline automates the process of building a Docker image, pushing it to Docker Hub, and deploying it to a Minikube cluster.

## Workflow Configuration

The GitHub Actions workflow is defined in the `.github/workflows/ci-cd-pipeline.yml` file. Below is a breakdown of the workflow configuration:

### Triggers

The workflow is triggered on the following events:
- `push` to the `main` branch
- `pull_request` targeting the `main` branch

### Jobs

The workflow consists of two main jobs: `build` and `deploy`.

#### Build Job

This job is responsible for building and pushing the Docker image.

- **Runs on:** `ubuntu-latest`

**Steps:**
1. **Checkout Code:**
   - Uses the `actions/checkout@v4` action to check out the repository code.
   
2. **Build Docker Image:**
   - Builds the Docker image using the Dockerfile in the repository.
   - Tags the image with the GitHub run number.

3. **Log in to Docker Hub:**
   - Logs in to Docker Hub using credentials stored in GitHub secrets.

4. **Push Docker Image:**
   - Pushes the Docker image to Docker Hub with the tag `${{ github.run_number }}`.

#### Deploy Job

This job is responsible for deploying the application to a Minikube cluster.

- **Runs on:** `ubuntu-20.04`
- **Needs:** `build` job to be completed

**Steps:**
1. **Checkout Code:**
   - Uses the `actions/checkout@v4` action to check out the repository code.

2. **Start Minikube:**
   - Uses the `medyagh/setup-minikube@latest` action to start Minikube.

3. **Configure kubectl:**
   - Configures `kubectl` to interact with the Minikube cluster.

4. **Install Ingress Controller:**
   - Enables the Ingress addon in Minikube and waits for it to be ready.

5. **Deploy to Kubernetes:**
   - Applies the Kubernetes manifests for Deployment, Service, and Ingress from the `yamls` directory.

6. **Wait for Deployment to Finish:**
   - Waits for the deployment to complete successfully.

7. **Check Pods Status:**
   - Retrieves and displays the status of the pods.

8. **Check Services Status:**
   - Retrieves and displays the status of the services.

9. **Check Ingress Status:**
   - Retrieves and displays the status of the ingress.

10. **Describe Ingress:**
    - Provides detailed information about the ingress.

11. **Run Health Check:**
    - Runs a health check by making a request to the application's health check endpoint.

12. **Test Main API Endpoint:**
    - Tests the main API endpoint by making a request to the `/characters` endpoint.

## Secrets

The following secrets must be configured in the GitHub repository settings:

- `DOCKER_USERNAME`: Your Docker Hub username.
- `DOCKER_PASSWORD`: Your Docker Hub password.

## Usage

To trigger the workflow, simply push changes to the `main` branch or create a pull request targeting the `main` branch. The workflow will automatically build, push, and deploy the application.


