pipeline {
    agent {
        node {
            label 'centos6'
        }
    }
    stages {
        stage('sanity') {
            agent any
            steps {
                sh 'echo "hi"'       
            }
        }
        stage('compile') {
            agent {
                    docker {
                        image 'quay.io/aaroc/code-rade-centos6'
                        label 'centos6'
                    }
                }
            environment {
                VERSION = "6.1.2"
                OS = "centos6"
                SITE = "generic"
                ARCH = "x86_64"
            }
            steps {
                    echo "building"
                    sh './build.sh'
                }
            }  // Build stage
        } // stages
} // pipeline