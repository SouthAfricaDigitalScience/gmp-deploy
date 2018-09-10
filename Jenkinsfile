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
                        label 'centos6'
                    }
                    steps('Build') {
                        sh './build.sh'
                    }
                }
                stage('centos7') {
                    agent {
                        label 'centos7'
                    }
                    steps('Build') {
                        sh './build.sh'
                    }
                }
            } // parallel
        }  // Build stage
    } // stages
} // pipeline