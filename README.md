**📁 Project Structure**

docker-microstack/
│
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── VotePage.js
│   │   └── ResultsPage.js
│   ├── nginx.conf
│   └── Dockerfile
│
├── nginx/
│   └── default.conf
│
├── docker-compose.yml
└── README.md

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

