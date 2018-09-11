pipeline {
  agent none
  stages {
    stage('build') {
      parallel {
        stage('build on centos6') {
          agent { 
            docker {
              image 'quay.io/aaroc/code-rade-centos:latest'   
              label "centos6"
            }
          }
          steps {
            sh './build.sh'
          }
        }
        stage('build on centos7') {
          agent { 
            docker {
              image 'quay.io/aaroc/code-rade-centos7:latest'
              label "centos7"
            }
          }
          steps {
            sh './build.sh'
          }
        }
      }
    }
  }
}