pipeline {
    stages {
        stage('sanity') {
            agent any
            steps {
                sh 'echo "hi"'
        }
        stage('Build') {
            steps {
                node('centos6') {
                    sh './build.sh'
                }
            }
        }
    }
}