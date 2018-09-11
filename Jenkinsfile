pipeline {
  agent {
    docker {
      image 'quay.io/aaroc/code-rade-centos:latest'
      label 'centos6'
    }
  }
  agent {
    docker {
      image 'quay.io/aaroc/code-rade-centos7:latest'
      label 'centos7'
    }
  }
  stages {
    stage('build') {
      parallel {
        stage('build on centos6') {
          agent { label "centos6"}
          steps {
            sh './build.sh'
          }
        }
        stage('build on centos7') {
          agent { label "centos7"}
          steps {
            sh './build.sh'
          }
        }
      }
    }
  }
}