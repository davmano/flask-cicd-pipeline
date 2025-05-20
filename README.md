# 🧰 Flask CI/CD Pipeline – DevOps Toolbox API

A lightweight Flask API built to showcase CI/CD skills, RESTful API development, and DevOps best practices. This project is ideal for testing request data, retrieving environment details, and integrating with cloud pipelines.

---

## 🚀 Features

| Endpoint      | Description                          |
|---------------|--------------------------------------|
| `/`           | Welcome message                      |
| `/ip`         | Returns the client IP address        |
| `/headers`    | Returns request headers              |
| `/env`        | Displays selected environment vars   |
| `/health`     | Health check endpoint                |

---

## ⚙️ Tech Stack

- **Backend**: Python, Flask  
- **Testing**: Pytest  
- **CI/CD**: GitHub Actions  
- **Containerization**: Docker  
- **Optional Deployment**: Render / Railway / Fly.io

---

## 📦 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/davmano/flask-cicd-pipeline.git
cd flask-cicd-pipeline
```

## 🐳 Docker Image

This project is available as a pre-built Docker image on Docker Hub.

### 📥 Pull and Run the Image

```bash
docker pull davmano/flask-cicd-toolbox
docker run -p 5000:5000 davmano/flask-cicd-toolbox
```

# 🧰 Flask CI/CD Pipeline – DevOps Toolbox API

![Build Status](https://github.com/davmano/flask-cicd-pipeline/actions/workflows/ci-cd.yml/badge.svg)

## 👨‍💻 Author

**David Mano**  
[GitHub](https://github.com/davmano)
