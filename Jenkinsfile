pipeline {
  agent none
  stages {
    stage('build') {
      parallel {
        stage('build on centos6') {
          agent { label "centos6" }
          steps {
            sh './build.sh'
          }
        }
        stage('build on centos7') {
          agent { label "sl7" }
          steps {
            sh './build.sh'
          }
      }
    }
  }
}