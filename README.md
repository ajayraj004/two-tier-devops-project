# 🚀 Two-Tier Web Application with Docker, Jenkins & AWS

A production style **Two-Tier Web Application** built with **Flask and MySQL**, containerized using **Docker and Docker Compose**, and deployed on **AWS EC2** with an automated **Jenkins CI/CD pipeline** integrated with GitHub Webhooks.

The project demonstrates how source code can automatically move from a developer's machine to a running application through a complete CI/CD workflow.

---

## 📌 Project Overview

This project implements a two-tier architecture:

- **Application Tier:** Python Flask web application
- **Database Tier:** MySQL database

Both components run as separate Docker containers and communicate through a private Docker network.

The application is deployed on an AWS EC2 instance and automatically updated whenever new code is pushed to the GitHub repository.

---

## 🏗️ Architecture

```text
                         👨‍💻 Developer
                              │
                              │ git push
                              ▼
                       ┌──────────────┐
                       │    GitHub    │
                       └──────┬───────┘
                              │
                         Webhook Event
                              │
                              ▼
                       ┌──────────────┐
                       │   Jenkins    │
                       │    CI/CD     │
                       └──────┬───────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                  Build                Deploy
                    │                   │
                    ▼                   ▼
              Docker Image       Docker Compose
                                        │
                         ┌──────────────┴──────────────┐
                         │                             │
                         ▼                             ▼
                  ┌─────────────┐              ┌─────────────┐
                  │    Flask    │              │    MySQL    │
                  │  Container  │─────────────▶│  Container  │
                  └──────┬──────┘              └─────────────┘
                         │
                         ▼
                    Port 5000
                         │
                         ▼
                      🌐 User
```

---

## 🔄 CI/CD Workflow

```text
Developer
   │
   │ git push
   ▼
GitHub Repository
   │
   │ GitHub Webhook
   ▼
Jenkins
   │
   ├── Checkout Source Code
   ├── Run Tests / Checks
   ├── Build Docker Image
   ├── Deploy using Docker Compose
   └── Verify Containers
   │
   ▼
AWS EC2
   │
   ├── Flask Container
   └── MySQL Container
   │
   ▼
Updated Application
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application programming language |
| Flask | Web application framework |
| MySQL | Relational database |
| Docker | Application containerization |
| Docker Compose | Multi-container orchestration |
| Jenkins | CI/CD automation |
| Git | Version control |
| GitHub | Source code management |
| GitHub Webhooks | Automatic CI/CD trigger |
| AWS EC2 | Cloud deployment |
| Linux | Server operating system |

---

# 📁 Project Structure

```text
two-tier-devops-project/
│
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── .dockerignore
├── .gitignore
└── README.md
```

---

# 🧩 Application Components

## 1. Flask Application

The Flask application provides the web interface and application endpoints.

### Home

```text
GET /
```

Displays the main application page.

### Health Check

```text
GET /health
```

Used to verify that the Flask application is running.

Expected response:

```text
OK
```

### Database Test

```text
GET /db-test
```

Tests connectivity between the Flask application and MySQL.

Expected response:

```text
MySQL connected successfully!
```

---

# 🐳 Docker Configuration

The application is containerized using Docker.

## Flask Container

The Flask application is built from the project's `Dockerfile`.

```text
Python
   ↓
Flask
   ↓
Docker Container
```

The container exposes:

```text
5000
```

## MySQL Container

MySQL runs as a separate container using the official MySQL Docker image.

The database uses a Docker volume so that database data can persist across container recreation.

---

# 🔗 Docker Network

The Flask and MySQL containers communicate through a dedicated Docker network.

```text
two-tier-network

       ┌─────────────┐
       │    Flask    │
       │  Container  │
       └──────┬──────┘
              │
              │ MySQL connection
              ▼
       ┌─────────────┐
       │    MySQL    │
       │  Container  │
       └─────────────┘
```

The Flask application connects to MySQL using the Docker Compose service name:

```text
mysql
```

instead of:

```text
localhost
```

---

# 🏥 Database Health Check

Docker Compose uses a MySQL health check before starting the Flask application.

This prevents the Flask application from attempting to connect to MySQL before the database is ready.

```text
MySQL starts
     ↓
MySQL health check
     ↓
Database becomes healthy
     ↓
Flask container starts
```

---

# 🔐 Environment Configuration

The application uses environment variables for database configuration.

Example:

```text
MYSQL_HOST=mysql
MYSQL_USER=root
MYSQL_PASSWORD=<your-password>
MYSQL_DB=devops
```

Sensitive credentials should never be committed to GitHub.

---

# ⚙️ Running the Application Locally

## Prerequisites

Install:

- Python 3
- Docker Desktop
- Git

## 1. Clone the repository

```bash
git clone https://github.com/ajayraj004/two-tier-devops-project.git
cd two-tier-devops-project
```

## 2. Create Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run using Docker Compose

```bash
docker compose up -d --build
```

## 5. Check containers

```bash
docker ps
```

Expected:

```text
two-tier-flask
two-tier-mysql
```

## 6. Open the application

```text
http://localhost:5000
```

## 7. Test application health

```text
http://localhost:5000/health
```

Expected:

```text
OK
```

## 8. Test MySQL connection

```text
http://localhost:5000/db-test
```

Expected:

```text
MySQL connected successfully!
```

---

# 🐳 Useful Docker Commands

### Start application

```bash
docker compose up -d
```

### Build and start

```bash
docker compose up -d --build
```

### Stop containers

```bash
docker compose down
```

### View running containers

```bash
docker ps
```

### View all containers

```bash
docker ps -a
```

### View Flask logs

```bash
docker logs two-tier-flask
```

### View MySQL logs

```bash
docker logs two-tier-mysql
```

### Follow Flask logs

```bash
docker logs -f two-tier-flask
```

---

# ☁️ AWS Deployment

The application is deployed on an **AWS EC2 instance**.

The EC2 server hosts:

```text
AWS EC2
│
├── Linux
├── Docker
├── Docker Compose
├── Jenkins
└── Two-Tier Application
    │
    ├── Flask Container
    └── MySQL Container
```

---

# 🔥 Jenkins CI/CD Pipeline

Jenkins automates the application deployment process.

The pipeline is defined using:

```text
Jenkinsfile
```

Pipeline stages:

```text
Checkout
   ↓
Test
   ↓
Build Docker Image
   ↓
Deploy
   ↓
Verify
```

## Jenkins Pipeline Stages

### 1. Checkout

Jenkins retrieves the latest source code from GitHub.

### 2. Test

The pipeline verifies the required runtime and Docker tools.

### 3. Docker Build

Jenkins builds the Flask Docker image.

```bash
docker build
```

### 4. Deployment

The application is deployed using Docker Compose.

```bash
docker compose down
docker compose up -d --build
```

### 5. Verification

Jenkins verifies that the Docker containers are running.

```bash
docker ps
```

---

# 🔔 GitHub Webhook Integration

GitHub Webhooks automatically trigger Jenkins when new code is pushed.

```text
git push
    ↓
GitHub
    ↓
GitHub Webhook
    ↓
Jenkins
    ↓
Jenkins Pipeline
    ↓
Docker Build
    ↓
Docker Compose
    ↓
Application Updated
```

This removes the need to manually start the Jenkins build after every code change.

---

# 🚀 Continuous Deployment Example

A developer modifies the application and runs:

```bash
git add .
git commit -m "Update application"
git push origin main
```

GitHub sends a webhook to Jenkins.

Jenkins automatically:

```text
1. Detects the push
2. Checks out the new code
3. Runs pipeline checks
4. Builds the Docker image
5. Deploys using Docker Compose
6. Verifies the containers
```

The updated application is then available on the EC2 server.

---

# 🔒 Security Considerations

- SSH access should preferably be restricted to the administrator's IP.
- MySQL port `3306` is not exposed publicly.
- Database credentials should not be committed to GitHub.
- `.env` files are excluded using `.gitignore`.
- MySQL communicates with Flask through the private Docker network.
- Jenkins is accessed through its configured port.

For production deployments, additional security controls such as HTTPS, a reverse proxy, IAM least privilege, secrets management, and restricted Jenkins access should be implemented.

---

# 📊 Ports

| Port | Service | Purpose |
|------|---------|---------|
| 22 | SSH | EC2 administration |
| 80 | HTTP | Web traffic |
| 5000 | Flask | Application access |
| 8080 | Jenkins | Jenkins web interface |
| 3306 | MySQL | Internal database communication |

> MySQL port 3306 is not exposed to the public internet.

---

# 🧪 Testing Checklist

```text
☑ Flask application loads
☑ /health endpoint returns OK
☑ Flask connects to MySQL
☑ Docker containers are running
☑ MySQL volume is mounted
☑ Jenkins pipeline completes successfully
☑ GitHub webhook reaches Jenkins
☑ Git push triggers Jenkins automatically
☑ New application changes are deployed automatically
```

---

# 🧠 DevOps Concepts Demonstrated

- Linux server administration
- AWS EC2
- Git and GitHub
- GitHub Webhooks
- CI/CD
- Jenkins Pipelines
- Jenkinsfile
- Docker
- Docker Images
- Docker Containers
- Docker Compose
- Container networking
- Docker volumes
- Application health checks
- Environment variables
- Automated deployments
- Basic cloud security
- Troubleshooting and log analysis

---

# 🔮 Future Improvements

- [ ] Docker Hub image publishing
- [ ] Nginx reverse proxy
- [ ] HTTPS with SSL/TLS
- [ ] AWS IAM least-privilege configuration
- [ ] AWS Secrets Manager / Parameter Store
- [ ] CloudWatch monitoring
- [ ] Automated rollback
- [ ] Blue-Green deployment
- [ ] Automated unit tests
- [ ] Code quality checks
- [ ] Infrastructure as Code using Terraform
- [ ] Kubernetes deployment
- [ ] Monitoring with Prometheus and Grafana

---

# 🎯 Learning Outcomes

This project demonstrates the complete path:

```text
Source Code
    ↓
Version Control
    ↓
Continuous Integration
    ↓
Containerization
    ↓
Automated Deployment
    ↓
Cloud Infrastructure
    ↓
Running Application
```

---

# 👨‍💻 Author

**Your Name**

Cloud & DevOps Enthusiast

### Technologies

```text
AWS • Linux • Docker • Jenkins • GitHub • Git • Python • Flask • MySQL
```

---

# ⭐ Project Highlights

```text
🐳 Dockerized Application
☁️ AWS EC2 Deployment
🔄 Jenkins CI/CD
🔔 GitHub Webhook Automation
🗄️ MySQL Database
🌐 Flask Web Application
💾 Persistent Database Volume
🏥 Health Checks
🔗 Docker Networking
```

---

## 📜 License

This project is intended for educational and portfolio purposes.
