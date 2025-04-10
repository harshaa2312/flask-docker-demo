pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/harshaa2312/flask-docker-demo.git'
            }
        }

        stage('Install Python') {
            steps {
                sh '''
                    apt update
                    apt install -y python3 python3-pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
