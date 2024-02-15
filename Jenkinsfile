import groovy.json.JsonSlurper


pipeline {
    agent {
        docker { image 'python:alpine' }
    }

    parameters {
        string(name: 'CONTEXT_ARGS', defaultValue: '{"key1":"value1","key2":"value2"}', description: '')
    }

    stages {
        stage('Build') {
            setps {
                script {
                    sh 'python3 -m pip install --upgrade pip || true'
                    sh 'python3 -m pip install -r requirements.txt || true'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def jsonSlurper = new JsonSlurper()
                    def object = jsonSlurper.parseText CONTEXT_ARGS
                    assert object instanceof Map
                    println object
                    println object.key1
                    println object.key2

                    sh 'python test.py ${CONTEXT_ARGS}'
                }
            }
        }
    }
}