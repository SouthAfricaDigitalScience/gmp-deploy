pipeline {
    agent none
    stages {
        stage('sanity') {
            agent master
            steps {
                sh 'echo "hi"'
            }
        }
        stage('compile') {
            parallel {
                stage('centos6') {
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
                }
             } // parallel
        }  // Build stage
    } // stages
} // pipeline