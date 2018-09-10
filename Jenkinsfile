pipeline {
  agent { label 'master' }
  stages {
    stage('Build') {
      environment {
        OS = 'centos6'
        NAME = 'gmp'
        VERSION = '6.1.2'
        ARCH = 'x86_64'
      }
      agent {
        docker {
          image 'quay.io/aaroc/code-rade-centos6:latest'
          args '-P '
        }
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
      agent {
        docker {
          image 'quay.io/aaroc/code-rade-centos6:latest'
          args '-P '
        }
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