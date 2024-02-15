import groovy.json.JsonSlurper


pipeline {
    agent {
        docker { image 'python:alpine' }
    }

    parameters {
        string(name: 'CONTEXT_ARGS', defaultValue: '{"key":"value"}', description: '')
    }

    stages {
        stage('Test') {
            steps {
                script {
                    def jsonSlurper = new JsonSlurper()
                    def object = jsonSlurper.parseText CONTEXT_ARGS
                    assert object instanceof Map
                    echo '${object}'
                    println object.key1
                    println object.key2
                }
            }
        }
    }
}