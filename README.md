# CRUD Web Application Using Docker & Kubernetes

## 📌 Project Overview

This project demonstrates the development and deployment of a containerized CRUD (Create, Read, Update, Delete) web application using Docker and Kubernetes.

The application is a Cloud-Based Student Management System built using Python Flask and deployed inside a Kubernetes cluster for orchestration and scalability.

---

## 🎯 Objectives

- Develop a CRUD-based web application
- Containerize the application using Docker
- Deploy the containerized application on Kubernetes
- Expose the application using Kubernetes Service
- Demonstrate container orchestration

---

## 🛠 Technology Stack

- Python Flask (Backend)
- HTML, CSS, JavaScript (Frontend)
- SQLite (Database)
- Docker (Containerization)
- Kubernetes (Orchestration)
- Docker Desktop (Local Kubernetes Cluster)

---

## 🏗 System Architecture

Browser  
↓  
Kubernetes Service (NodePort / Port-Forward)  
↓  
Deployment  
↓  
Pod  
↓  
Docker Container (Flask App)  
↓  
SQLite Database  

---

## 🚀 Features

- Add Student
- View Students
- Delete Student
- Real-time Student Count
- Docker containerized environment
- Kubernetes-based deployment
- Exposed using Service

---

## 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t student-management-app .
