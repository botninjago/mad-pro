pipeline {
    agent {
        dockerfile true
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