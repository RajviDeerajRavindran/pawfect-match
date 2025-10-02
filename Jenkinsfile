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
                echo 'Running automated tests...'
                bat 'pip install pytest pytest-flask'
                bat 'pytest test_app.py -v'
            }
        }
        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to STAGING environment...'
                bat 'docker stop pawfect-staging || exit 0'
                bat 'docker rm pawfect-staging || exit 0'
                bat 'docker run -d --name pawfect-staging -p 5001:5000 pawfect-match:latest'
                echo 'Staging environment deployed to http://localhost:5001'
            }
        }
        stage('Deploy to Production') {
            steps {
                echo 'Deploying to PRODUCTION environment (Blue-Green)...'
                bat 'docker stop pawfect-production || exit 0'
                bat 'docker rm pawfect-production || exit 0'
                bat 'docker run -d --name pawfect-production -p 5000:5000 pawfect-match:latest'
                echo 'Production environment deployed to http://localhost:5000'
            }
        }
    }
}





