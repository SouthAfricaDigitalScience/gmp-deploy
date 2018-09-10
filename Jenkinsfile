pipeline {
  agent {
    docker {
      image 'quay.io/aaroc/code-rade-centos6:latest'
      args '-P '
    }
  }
  stages {
    stage('Build') {
      environment {
        OS = 'centos6'
        NAME = 'gmp'
        VERSION = '6.1.2'
        ARCH = 'x86_64'
      }
      steps {
        sh './build'
      }
    }
    stage('Test') {
      environment {
        OS = 'centos6'
        NAME = 'gmp'
        VERSION = '6.1.2'
        ARCH = 'x86_64'
      }
      steps {
        sh './check-build.sh'
      }
    }
    stage('Deliver') {
      environment {
        OS = 'centos6'
        NAME = 'gmp'
        VERSION = '6.1.2'
        ARCH = 'x86_64'
      }
      steps {
        sh './deploy'
      }
    }
  }
}