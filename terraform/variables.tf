variable "app_name" {
  description = "Application name"
  type        = string
  default     = "pawfect-match"
}

variable "app_replicas" {
  description = "Number of application replicas"
  type        = number
  default     = 2
}

variable "app_port" {
  description = "Application port"
  type        = number
  default     = 5000
}

variable "namespace" {
  description = "Kubernetes namespace"
  type        = string
  default     = "pawfect-match-ns"
}

variable "cpu_limit" {
  description = "CPU limit for containers"
  type        = string
  default     = "500m"
}

variable "memory_limit" {
  description = "Memory limit for containers"
  type        = string
  default     = "512Mi"
}
