pipeline {
  agent none
  stages {
    stage('Build') {
      node('x86_64 centos6') { 
        environment {
          OS = 'centos6'
          NAME = 'gmp'
          VERSION = '6.1.2'
          ARCH = 'x86_64'
        }
        steps {
          sh './build.sh'
          sh './check-build.sh'
        }
      }
    }
  }
}