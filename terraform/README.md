# Terraform Infrastructure as Code

## Overview
Terraform configuration for provisioning and managing Pawfect Match infrastructure on Docker and Kubernetes.

## Files
- **main.tf** - Main infrastructure configuration
- **variables.tf** - Variable definitions
- **outputs.tf** - Output values after deployment

## Resources Created
1. **Docker Image** - Builds application container
2. **Kubernetes Namespace** - Isolated environment (pawfect-match-ns)
3. **Kubernetes Deployment** - 2 replicas with resource limits
4. **Kubernetes Service** - NodePort service on port 30000

## Usage

### Initialize Terraform
terraform init

### Validate Configuration
terraform validate

### Preview Changes
terraform plan


### Apply Infrastructure
terraform apply


### Destroy Infrastructure
terraform destroy


## Variables
- `app_name` - Application name (default: pawfect-match)
- `app_replicas` - Number of replicas (default: 2)
- `app_port` - Application port (default: 5000)
- `namespace` - Kubernetes namespace (default: pawfect-match-ns)
- `cpu_limit` - CPU limit (default: 500m)
- `memory_limit` - Memory limit (default: 512Mi)

## Outputs
- `deployment_name` - Name of Kubernetes deployment
- `service_name` - Name of Kubernetes service
- `namespace` - Kubernetes namespace
- `service_port` - NodePort for external access
- `replicas` - Number of running replicas
