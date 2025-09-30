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
        stage('Deploy') {
            steps {
                echo 'Deploying green version...'
            }
        }
    }
}



