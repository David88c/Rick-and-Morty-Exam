### Overview

This project contains a Dockerfile to create a Docker image for a web application that provides information about characters from the Rick and Morty TV show. The application is built with Python and Flask.

### Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Docker on your machine. You can download it from [Docker's official site](https://www.docker.com/products/docker-desktop).

### Getting Started

Follow these instructions to get the project up and running on your local machine.

### Cloning the Repository

Clone the repository to your local machine using:

git clone https://github.com/David88c/Rick-and-Morty-Exam.git
 
### Building the Docker image

docker build -t rick-and-morty-app .

### Run Docker image

docker run -p 5000:5000 --name rick-and-morty-app -d  rick-and-morty-app