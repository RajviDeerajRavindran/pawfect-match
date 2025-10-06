# Ansible Automation for Pawfect Match

## Overview
Ansible playbooks for automated deployment and configuration management of the Pawfect Match application on Kubernetes.

## Files

### Configuration Files
- **inventory.ini** - Defines target hosts (local and Kubernetes)
- **ansible.cfg** - Ansible configuration settings

### Playbooks

#### 1. deploy-app.yml
Automates the complete application deployment process:
- Verifies Docker installation
- Builds Docker image from source
- Loads image into Minikube
- Deploys application to Kubernetes
- Waits for pods to be ready
- Displays deployment status

#### 2. configure-monitoring.yml
Sets up monitoring infrastructure:
- Deploys Prometheus for metrics collection
- Deploys Grafana for visualization
- Waits for services to be ready
- Displays monitoring service status

## Usage (Linux/WSL Environment)

### Deploy Application
ansible-playbook deploy-app.yml

### Configure Monitoring Stack
ansible-playbook configure-monitoring.yml

### Run Both Playbooks
ansible-playbook deploy-app.yml and configure-monitoring.yml


## Requirements
- Ansible 2.9+
- Docker
- Kubernetes/Minikube
- kubectl

## Note
Ansible requires a Linux/WSL environment to execute. These playbooks are designed to demonstrate configuration management and automation concepts as part of the DevOps pipeline.

## Architecture Benefits
- **Idempotent** - Can run multiple times safely
- **Automated** - Reduces manual deployment errors
- **Repeatable** - Consistent deployments across environments
- **Version Controlled** - Infrastructure as code



