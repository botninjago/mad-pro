import groovy.json.JsonSlurper
import groovy.json.JsonOutput

pipeline {
    agent {
        docker { 
            image 'python:alpine'
            // args '-u root'
        }
    }

    parameters {
        string(name: 'CONTEXT_ARGS', defaultValue: '{"key1":"value1","key2":"value2"}', description: '')
    }

    stages {
        // stage('Checkout') {
        //     steps {
        //         checkout scm
        //     }
        // }
        stage('Build') {
            steps {
                script {
                    withPythonEnv('python3') {
                        sh 'python3 -m pip install --upgrade pip || true'
                        sh "python3 -m pip install --target ${env.WORKSPACE} -r requirements.txt || true"
                    }
                }        
            }
        }
        // stage('Test') {
        //     steps {
        //         script{
        //             withPythonEnv('python3') {
        //                 sh 'python3 -m pytest -v'
        //             }
        //         }
        //     }
        // }
        stage('Model') {
            steps {
                script {
                    models = readJSON file: 'models.json'
                    models = models[0..<models.size()]
                    echo "${models}"

                    withPythonEnv('python3') {
                        sh 'python3 run.py ${CONTEXT_ARGS}'                    
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
        stage('Delete') {
            steps {
                echo 'Cleanup'
                cleanWs()
            }
        }
    }
}
