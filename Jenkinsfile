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
            parallel centos6: {
                node('centos6') {
                    steps('Build') {
                        sh './build.sh'
                    }
                }
            },
            centos7: {
                node('centos7') {
                    steps('Build') {
                        sh './build.sh'
                    }
                }
            }
        }  // stage
    } // stages
} // pipeline