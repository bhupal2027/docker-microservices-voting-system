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

