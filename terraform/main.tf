terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.23"
    }
  }
  required_version = ">= 1.0"
}

provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

# Docker Image Resource
resource "docker_image" "pawfect_match" {
  name = "pawfect-match:latest"
  build {
    context    = "../"
    dockerfile = "Dockerfile"
  }
}

# Kubernetes Namespace
resource "kubernetes_namespace" "pawfect_match" {
  metadata {
    name = "pawfect-match-ns"
  }
}

# Kubernetes Deployment
resource "kubernetes_deployment" "pawfect_match" {
  metadata {
    name      = "pawfect-match-deployment"
    namespace = kubernetes_namespace.pawfect_match.metadata[0].name
    labels = {
      app = "pawfect-match"
    }
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = "pawfect-match"
      }
    }

    template {
      metadata {
        labels = {
          app = "pawfect-match"
        }
      }

      spec {
        container {
          name  = "pawfect-match"
          image = docker_image.pawfect_match.name

          port {
            container_port = 5000
          }

          resources {
            limits = {
              cpu    = "500m"
              memory = "512Mi"
            }
            requests = {
              cpu    = "250m"
              memory = "256Mi"
            }
          }
        }
      }
    }
  }
}

# Kubernetes Service
resource "kubernetes_service" "pawfect_match" {
  metadata {
    name      = "pawfect-match-service"
    namespace = kubernetes_namespace.pawfect_match.metadata[0].name
  }

  spec {
    selector = {
      app = "pawfect-match"
    }

    port {
      port        = 5000
      target_port = 5000
      node_port   = 30000
    }

    type = "NodePort"
  }
}
