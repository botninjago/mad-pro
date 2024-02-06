pipeline {
    agent {
        docker { image 'python:alpine' }
    } 
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Hello world!' 
                sh 'python -V'
            }
        }
    }
}