import groovy.json.JsonSlurper


pipeline {
    agent {
        docker { image 'python:alpine' }
    }

    parameters {
        string(name: 'CONTEXT_ARGS', defaultValue: '{"key1":"value1","key2":"value2"}', description: '')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {
                withPythonEnv('python3') {
                    sh 'python3 -m pytest'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    withPythonEnv('python3') {
                        sh 'python3 -m pip install --upgrade pip || true'
                        sh 'python3 -m pip install -r requirements.txt || true'
                        sh 'python3 example.py ${CONTEXT_ARGS}'                    
                    }

                    // def jsonSlurper = new JsonSlurper()
                    // def object = jsonSlurper.parseText CONTEXT_ARGS
                    // assert object instanceof Map
                    // println object
                    // println object.key1
                    // println object.key2
                    
                    echo "${env.NODE_NAME}, ${env.JOB_NAME}, ${env.arch}"
                    echo "${env.BUILD_USER}, ${env.BUILD_NUMBER}, ${env.BUILD_URL}"
                }
            }
        }
    }
}
