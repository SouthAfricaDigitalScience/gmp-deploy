pipeline {
  agent none
  stages {
    node('x86_64 centos6') { 
      stage('Build') {
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