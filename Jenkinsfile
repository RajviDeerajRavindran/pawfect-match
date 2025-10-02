pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building Pawfect Match...'
                bat 'python --version'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t pawfect-match:latest .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing app...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying blue-green...'
                bat 'docker stop pawfect-blue || exit 0'
                bat 'docker rm pawfect-blue || exit 0'
                bat 'docker run -d --name pawfect-blue -p 5000:5000 pawfect-match:latest'
                echo 'Application deployed to http://localhost:5000'
            }
        }
    }
}





