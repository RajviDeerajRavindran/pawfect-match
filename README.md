# Pawfect Match

Pawfect Match is a caring platform dedicated to connecting pets with loving homes, with a special focus on stray dogs in India. Built using HTML, CSS, JavaScript, and Flask, our lightweight application stores pet information in a JSON file and delivers a smooth, interactive experience. The platform also leverages a Blue-Green Deployment strategy with Docker and Nginx to ensure zero downtime during updates, making adoption simple, reliable, and accessible for everyone.
This project implements a DevOps CI/CD pipeline for a web application that helps connect stray pets with adopters, featuring automated deployment and monitoring.


## Technology Stack

### Application
- **Backend:** Python Flask
- **Testing:** pytest, pytest-flask
- **Containerization:** Docker

### DevOps Tools
- **Version Control:** Git
- **CI/CD:** Jenkins
- **Container Orchestration:** Kubernetes (Minikube)
- **Configuration Management:** Ansible
- **Infrastructure as Code:** Terraform
- **Monitoring:** Prometheus + Grafana
- **Security Scanning:** Trivy

## Project Structure
pawfect-match/
├── app.py # Main Flask application
├── Dockerfile # Container image definition
├── requirements.txt # Python dependencies
├── test_app.py # Automated tests
├── Jenkinsfile # CI/CD pipeline definition
├── deployment.yaml # Kubernetes deployment
├── service.yaml # Kubernetes service
├── prometheus-config.yaml # Prometheus configuration
├── grafana.yaml # Grafana deployment
├── ansible/ # Ansible playbooks
│ ├── deploy-app.yml
│ ├── configure-monitoring.yml
│ └── inventory.ini
├── terraform/ # Infrastructure as Code
│ ├── main.tf
│ ├── variables.tf
│ └── outputs.tf
└── SECURITY.md # Security scan results

## Quick Start

### Prerequisites
- Docker
- Kubernetes/Minikube
- Python 3.9+
- Jenkins
- Git


### Local Development
Clone repository
git clone <repo-url>
cd pawfect-match

Install dependencies
pip install -r requirements.txt

Run application
python app.py

Run tests
pytest test_app.py -v


### Docker
Build image
docker build -t pawfect-match:latest .

Run container
docker run -p 5000:5000 pawfect-match:latest


### Kubernetes Deployment
Start Minikube
minikube start

Deploy application
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Deploy monitoring
kubectl apply -f prometheus-config.yaml
kubectl apply -f grafana.yaml

Access services
minikube service pawfect-match-service
minikube service prometheus-service
minikube service grafana-service


### Terraform
cd terraform
terraform init
terraform plan
terraform apply


### Ansible
cd ansible
ansible-playbook deploy-app.yml
ansible-playbook configure-monitoring.yml

text

## CI/CD Pipeline

The Jenkins pipeline automates:
1. **Build** - Docker image creation
2. **Test** - Automated testing with pytest
3. **Security Scan** - Container vulnerability scanning
4. **Deploy** - Kubernetes deployment
5. **Monitor** - Prometheus & Grafana setup
6. **Staging** - Staging environment (port 5001)
7. **Production** - Production deployment (port 5000)

## Monitoring

### Prometheus
- Metrics collection
- URL: `minikube service prometheus-service`

### Grafana
- Metrics visualization
- URL: `minikube service grafana-service`
- Default credentials: admin/admin

### Dashboards
- HTTP Requests Total
- Average Request Duration
- Memory Usage
- CPU Usage

## Security

Security scanning performed with Trivy:
- 0 Critical vulnerabilities
- 3 High severity issues (resolved)
- See `SECURITY.md` for details

## Deployment Environments

- **Development:** http://localhost:5000
- **Staging:** http://localhost:5001
- **Production (Docker):** http://localhost:5000
- **Production (Kubernetes):** `minikube service pawfect-match-service`

## Testing

Run all tests
pytest test_app.py -v

Run with coverage
pytest test_app.py --cov=app --cov-report=html

text

## Team
- Rajvi Deeraj R
- Surya KP

