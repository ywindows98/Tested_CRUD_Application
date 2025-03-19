# Tested Full-Stack Dockerized Web Application

A tested full-stack web application that uses modern technologies and best practices. This project integrates a Python-based backend using Flask and SQLAlchemy, a simple but dynamic React frontend for a demonstration, and a PostgreSQL database—all containerized using Docker. Tests have been implemented for the backend to ensure reliability using unittest and pytest.

---

## Project Purpose 

The primary goal of this project was to explore and master a variety of new technologies and methodologies. Through this project, I aimed to:

- **Expand Technical Expertise:**  
  Experiment with and integrate technologies such as Python (Flask, SQLAlchemy, unittest, pytest), React, PostgreSQL, Docker. I also aimed to build a solid project architecture, use design patterns throughout the code and apply best-practice recommendations for software development and testing.
  
- **Embrace Test-Driven Development (TDD):**  
  Implement automated tests using unittest and pytest to ensure high code quality, reliability, and to adopt TDD practices as a core part of the development process.

This project is a testament to my commitment to continuous learning, improving my skills in using modern technologies, software development and testing methods.

---

## Features

- **Modular Architecture:** Clear separation between backend, frontend, and database.
- **Backend:** Built with Python, Flask, and SQLAlchemy.
- **Frontend:** Developed in React with JavaScript.
- **Database:** Utilizes PostgreSQL for data storage.
- **Containerization:** Docker and Docker Compose are used to streamline development, testing, and deployment.
- **Testing:** Integrated unittests for the backend to ensure quality and .
- **Automation Scripts:** Bash scripts (`start-app.sh` and `end-app.sh`) simplify starting and stopping the entire application.

---

### How to Use

1. **Clone the Repository:**
2. **Start the Application:**
Use the provided bash script to build and run the Docker containers: ```./start-app.sh```. Tests for the backend are run automatically before backend launch.


4. **Accessing the App:**
Once started, the backend will be available on its configured port 5000 on localhost, and the frontend on port 3000 on localhost.

5. **Stopping and Cleaning Up:**
When you're ready to stop the application and clear the Docker environment, use the provided bash script: ```./end-app.sh```. This script stops all running containers and removes them along with any associated networks and volumes.


