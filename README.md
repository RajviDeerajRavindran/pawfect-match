# Pawfect Match (Rajvi Deeraj R, Surya KP)

Pawfect Match is a caring platform dedicated to connecting pets with loving homes, with a special focus on stray dogs in India. Built using HTML, CSS, JavaScript, and Flask, our lightweight application stores pet information in a JSON file and delivers a smooth, interactive experience. The platform also leverages a Blue-Green Deployment strategy with Docker and Nginx to ensure zero downtime during updates, making adoption simple, reliable, and accessible for everyone.
This project implements a DevOps CI/CD pipeline for a web application that helps connect stray pets with adopters, featuring automated deployment and monitoring.

## Architecture Diagram
(You can add or sketch this separately)

## Tools Used and Justification
- **Git/GitHub**: Version control and collaboration
- **Jenkins**: CI/CD pipeline automation
- **Docker**: Containerization for consistent deployment
- **Docker Compose**: Multi-container orchestration
- **Python Flask**: Web application framework
- **Monitoring**: (Prometheus/Grafana if implemented)
- **Configuration Management**: (Ansible, if implemented)
- **Infrastructure as Code**: (Terraform, if implemented)

## CI/CD Pipeline Implementation
- Automated build, test, and deployment using Jenkins
- Automated testing with pytest
- Staging and production environments via Docker
- Blue-green deployment approach using separate containers and ports

## Deployment Instructions
1. **Build Docker image**: `docker build -t pawfect-match:latest .`
2. **Run directly:**
   - Production: `docker run -d --name pawfect-production -p 5000:5000 pawfect-match:latest`
   - Staging: `docker run -d --name pawfect-staging -p 5001:5000 pawfect-match:latest`
3. **Alternatively, use Docker Compose:**
   - `docker-compose up`
   - Access production: http://127.0.0.1:5000, staging: http://127.0.0.1:5001

## Monitoring and Security
- Monitoring tools (Prometheus/Grafana/ELK) setup details
- DevSecOps practices applied

## Project Documentation
- This README.md describes project architecture, tool choices, and usage instructions.
- All code and pipeline configurations are documented inline.

