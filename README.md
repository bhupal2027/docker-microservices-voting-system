**📌 Overview**

This project implements a complete microservices architecture where each component runs in its own Docker container.
Users can vote for Cat or Dog and view live results, which are fetched from the backend and stored in PostgreSQL.

This setup is ideal for DevOps, Cloud, and SRE portfolio work.

**✨ Features**

**🟦 React Frontend**

/vote → Vote for Cat or Dog

/results → Live updated results

Uses React Router

Clean, simple UI

**⬛ Flask Backend**

/api/vote → Submit a vote

/api/votes → Get total counts

Connects to PostgreSQL

Exposed internally on port 8000

**🐘 PostgreSQL Database**

Stores every vote:

CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    animal TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

**🟩 Redis + Celery (Ready for background tasks)**

Currently included and running, can be extended for async processing.

**🟢 NGINX Reverse Proxy**

Handles routing:

URL Path	Routed To

/ → React frontend

/vote → React frontend

/results → React frontend

/api/* → Flask backend

**🐳 Fully Dockerized**

Containers communicate through Docker networks

No manual installation required

Easy to run and extend

**Architecture Diagram**





**📁 Project Structure**

https://github.com/bhupal2027/docker-microservices-voting-system/blob/2e0b7ad52b5eeb8f72b30d0e977540744f7f85c9/Project_Structure.png



**🔍 How It Works (Workflow Summary)**

**✔ Voting Flow**

User clicks “Vote Cat” or “Vote Dog.”

React sends POST /api/vote

NGINX forwards to the backend

Flask inserts a vote into PostgreSQL

React automatically refreshes results

**✔ Results Flow**

React polls /api/votes

Backend queries DB

React displays updated counts

**🎯 What You Learn / Demonstrate**

This project shows:

Microservices architecture

Routing with NGINX reverse proxy

API + frontend + DB integration

Container networking

Docker Compose orchestration

Production-like environment

