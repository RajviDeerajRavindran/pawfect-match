pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building Pawfect Match...'
                bat 'python --version'  // Windows batch command
            }
        }
        stage('Test') {
            steps {
                echo 'Testing app...'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t pawfect-match:latest .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying blue-green...'
                bat 'docker stop pawfect-blue || exit 0'
                bat 'docker rm pawfect-blue || exit 0'
                bat 'docker run -d --name pawfect-green -p 5001:5000 pawfect-match:latest'
                echo 'Green deployed—test at http://localhost:5001'
            }
        }
    }
}



