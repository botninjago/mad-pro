import groovy.json.JsonSlurper


pipeline {
    agent {
        docker { image 'python:alpine' }
    }

    parameters {
        string(name, 'CONTEXT_ARGS', defaultValue: '{"key1": "value1", "key2": "value2"}', description: '')
    }

    stages {
        stage('Test') {
            steps {
                script {
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