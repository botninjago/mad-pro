pipeline {
    agent {
        docker { image 'python:alpine' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python3 --version'
            }
        }
    }
}