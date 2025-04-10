pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/harshaa2312/flask-docker-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Flask Container') {
            steps {
                sh 'docker run -d -p 5000:5000 flask-app'
            }
        }
    }
}
