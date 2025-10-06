output "deployment_name" {
  description = "Name of the Kubernetes deployment"
  value       = kubernetes_deployment.pawfect_match.metadata[0].name
}

output "service_name" {
  description = "Name of the Kubernetes service"
  value       = kubernetes_service.pawfect_match.metadata[0].name
}

output "namespace" {
  description = "Kubernetes namespace"
  value       = kubernetes_namespace.pawfect_match.metadata[0].name
}

output "service_port" {
  description = "Service NodePort"
  value       = kubernetes_service.pawfect_match.spec[0].port[0].node_port
}

output "replicas" {
  description = "Number of replicas"
  value       = kubernetes_deployment.pawfect_match.spec[0].replicas
}
