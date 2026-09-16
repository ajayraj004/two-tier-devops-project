pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Running application checks...'
                sh 'python3 --version'
                sh 'docker --version'
                sh 'docker compose version'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t two-tier-flask-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'

                sh 'docker compose down || true'

                sh 'docker compose up -d --build'
            }
        }

        stage('Verify') {
            steps {
                echo 'Checking containers...'
                sh 'docker ps'
            }
        }
    }

    post {

        success {
            echo '🎉 Deployment successful!'
        }

        failure {
            echo '❌ Deployment failed!'
        }
    }
}