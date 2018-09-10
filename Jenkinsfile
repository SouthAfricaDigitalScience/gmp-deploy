pipeline {
  agent {
    node {
      label 'centos6'
    }
  }
  stages {
    stage('sanity') {
      environment {
        VERSION = '6.1.2'
        OS = 'centos6'
        SITE = 'generic'
        ARCH = 'x86_64'
      }
      agent { 
          docker {
              reuseNode true
              image 'quay.io/aaroc/code-rade-centos6'
          }
      }
      steps {
        sh 'echo "hi"'
        sh './build.sh'
      }
    }
  }
}