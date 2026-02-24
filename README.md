# Emotion Classifier App 🎭

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![NLP](https://img.shields.io/badge/NLP-Text%20Classification-purple)
![TF-IDF](https://img.shields.io/badge/Feature%20Engineering-TF--IDF-8A2BE2)
![Bag of Words](https://img.shields.io/badge/Feature%20Engineering-Bag%20of%20Words-6A5ACD)
![Logistic Regression](https://img.shields.io/badge/Model-Logistic%20Regression-yellow)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![AWS EC2](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonaws)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub%20Actions-2088FF?logo=githubactions)

A Dockerized Emotion Classification Web Application deployed on AWS EC2 with CI/CD using GitHub Actions.

---

## 🚀 Live Demo

🔗 [Live Application](http://16.171.5.109/)

---

## 📌 Project Overview

This project is an end-to-end Emotion Classification system that:

- Accepts user text input
- Uses a trained ML model to classify emotion
- Displays prediction via Streamlit frontend
- Exposes API using FastAPI backend

This project demonstrates how to build, containerize, and deploy a production-ready NLP model with automated CI/CD on AWS.
It highlights full-stack ML capabilities from preprocessing to cloud deployment.

---

## 🧠 Machine Learning Pipeline

### 🔹 Problem Type
- Classification

### 🔹 Target Variable
- `emotion`

### 🔹 Final Feature Set
- text 
- emotion

### 🔹 Output class
- sadness
- anger
- love
- surprise
- fear
- joy

### 🔹 Text Cleaning
- lowercasing
- Remove punctuation, numbers, emojis, and stopwords

### 🔹 Text Vectorization
- Bag of Words
- TF-IDF 

---

## 🤖 Model Training & Evaluation

### Modeling and Hyperparameter tuning
- Naive Bayes
- **Logistic Regression**
- GridSearchCV

### Final Model Performance
**Weighted F1-score: 0.90**

---

## 🔁 CI/CD Pipeline (GitHub Actions)

- On every push to main branch:
    - Trigger: Push to `main` branch
    - Secure SSH connection to AWS EC2
    - Pull latest repository changes
    - Rebuild Docker images
    - Restart containers automatically

---

## 🏗 System Architecture

  User  
   │  
   ▼  
Streamlit (Frontend)  
   │  
   ▼  
FastAPI (Backend)  
   │  
   ▼  
ML Model  
   │  
   ▼  
Docker Containers  
   │  
   ▼  
AWS EC2  

---

## 🧰 Tech Stack

- Python
- FastAPI
- Streamlit
- Docker
- Docker Compose
- AWS EC2
- GitHub Actions (CI/CD)

---

## 🏁 How to Run Locally

Clone the repository:

git clone https://github.com/TanuDewangan/emotion-classifier-app.git

cd emotion-classifier-app

Build and run using Docker:

docker-compose up --build

Access:
Frontend → http://localhost:8501  
Backend Docs → http://localhost:8000/docs

---

## 📈 Future Enhancements

- Add HTTPS (SSL certificate)
- Add custom domain
- Add monitoring & logging
- Deploy using Docker Hub image

---

## 👤 Author

**Tanu Dewangan**  
NLP | Machine Learning | Data Science | End-to-End ML Systems

🔗 GitHub: https://github.com/TanuDewangan 

---