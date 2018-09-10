pipeline {
    agent any
    stages {
        stage('sanity') {
            agent any
            steps {
                sh 'echo "hi"'
            }
        }
        stage('Build') {
            agent {
                docker {
                    image 'quay.io/aaroc/code-rade-centos6'
                    label 'centos6'
                }
            }
            agent {
                docker {
                    image 'quay.io/aaroc/code-rade-centos7'
                    label 'centos7'
                }
            }
            parallel {
                stage('centos6') {
                    environment {
                        VERSION = "6.1.2"
                        OS = "centos6"
                        SITE = "generic"
                        ARCH = "x86_64"
                    }
                    node('centos6')
                    steps('Build') {
                        sh './build.sh'
                    }
                }
             } // parallel
        }  // Build stage
    } // stages
} // pipeline