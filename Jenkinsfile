pipeline {
  agent none
  environment {
    ARCH = 'x86_64'
    SITE = 'generic'
    NAME = 'gmp'
  }
  stages {
    stage('build') {
      parallel {
        stage('build 6.1.2 on centos6') {
          environment {
            OS = 'centos6'
            VERSION = '6.1.2'
          }
          agent { label "centos6" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
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
}