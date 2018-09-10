pipeline {
  agent Jenkins
  stages {
    stage('build') {
      agent {
        docker {
          image 'quay.io/aaroc/code-rade-centos6:latest'
        }
      }
      environment {
        HOME = '/home/jenkins'
        VERSION = '6.1.2'
        OS = 'centos6'
        SITE = 'generic'
        NAME = 'gmp'
      }
      steps {
        sh 'ls'
        sh './build.sh'
      }
    }
  }
}
