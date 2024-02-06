pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Hello world!' 
                sh 'pwd'
                sh 'ls'
                sh 'python3 --version'
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh 'pip freeze'
            }
        }
    }
}