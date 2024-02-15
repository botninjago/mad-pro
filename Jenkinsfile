pipeline {
    agent {
        docker { image 'python:alpine' }
    }
    stages {
        stage('Test') {
            steps {
                script {
                    def jsonString = '{"key1": "value1", "key2": "value2"}'
                    def jsonObject = readJSON text: jsonString
                    echo "JSON Object: ${jsonObject}"
                }
            }
        }
    }
}