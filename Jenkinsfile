pipeline {
    agent none
    stages {
        stage('sanity') {
            agent any
            steps {
                sh 'echo "hi"'
            }
        }
        stage('Build') {
            parallel {
                stage('centos6') {
                    agent {
                        docker {
                            image 'quay.io/aaroc/code-rade-centos6'
                        }
                    }
                    steps('Build') {
                        sh './build.sh'
                    }
                }
                stage('centos7') {
                    agent {
                        docker {
                            image 'quay.io/aaroc/code-rade-centos7'
                        }
                    }
                    steps('Build') {
                        sh './build.sh'
                    }
                }
            } // parallel
        }  // Build stage
    } // stages
} // pipeline