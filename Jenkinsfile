pipeline {
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
                    node('centos6')
                    steps('Build') {
                        sh './build.sh'
                    }
                }
                stage('centos7') {
                    node('centos7')
                    steps('Build') {
                        sh './build.sh'
                    }
                }
            } // parallel
        }  // Build stage
    } // stages
} // pipeline