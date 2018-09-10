pipeline {
  agent {
    docker {
      image 'quay.io/aaroc/code-rade-centos6:latest'
    }
  }
  stages {
    stage('build') {
      steps {
        sh './build.sh'
      }
    }
    stage('test') {
      steps {
        sh './check-build.sh'
      }
    }
    stage('deploy') {
      steps {
        sh './deploy.sh'
      }
    }
  }
}