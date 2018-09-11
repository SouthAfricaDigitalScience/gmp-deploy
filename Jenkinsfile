pipeline {
  agent {
    label 'master'
  }
  environment {
    ARCH = 'x86_64'
    SITE = 'generic'
    NAME = 'gmp'
  }
  stages {
    stage('sanity') {
      fileExists 'build.sh'
      fileExists 'check-build.sh'
      fileExists 'deploy.sh'
    }
    stage('build') {
      parallel {
        stage('build 6.1.2 on centos6') {
          environment {
            OS = 'centos6'
            VERSION = '6.1.2'
            WORKSPACE = '/home/jenkins/workspace/$NAME/'
          }
          agent { label "centos6" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './build.sh'
          }
        }
        stage('build 6.1.0 on centos6') {
          environment {
            OS = 'centos6'
            VERSION = '6.1.0'
          }
          agent { label "centos6" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './build.sh'
          }
        }
        stage('build 6.1.2 on centos7') {
          environment {
            OS = 'centos7'
            VERSION = '6.1.2'
          }
          agent { label "centos7" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './build.sh'
          }
        }
        stage('build 6.1.0 on centos7') {
          environment {
            OS = 'centos7'
            VERSION = '6.1.0'
          }
          agent { label "centos7" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './build.sh'
          }
        }
        stage('build 6.1.2 on ubuntu 1404') {
          environment {
            OS = 'u1404'
            VERSION = '6.1.2'
          }
          agent { label "u1404" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './build.sh'
          }
        }
        stage('build 6.1.0 on ubuntu 1404') {
          environment {
            OS = 'u1404'
            VERSION = '6.1.0'
          }
          agent { label "u1404" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './build.sh'
          }
        }
        stage('build 6.1.2 on ubuntu 1610') {
          environment {
            OS = 'centos6'
            VERSION = '6.1.2'
          }
          agent { label "u1610" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './build.sh'
          }
        }
        stage('build 6.1.0 on ubuntu 1610') {
          environment {
            OS = 'u1610'
            VERSION = '6.1.0'
          }
          agent { label "u1610" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './build.sh'
          } // steps
        } // stage
      } // parallel
    } // stage build
    stage('test') {
      parallel {
        stage('test 6.1.2 on centos6') {
          environment {
            OS = 'centos6'
            VERSION = '6.1.2'
          }
          agent { label "centos6" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './check-build.sh'
          }
        }
        stage('test 6.1.0 on centos6') {
          environment {
            OS = 'centos6'
            VERSION = '6.1.0'
          }
          agent { label "centos6" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './check-build.sh'
          }
        }
        stage('test 6.1.2 on centos7') {
          environment {
            OS = 'centos7'
            VERSION = '6.1.2'
          }
          agent { label "centos7" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './check-build.sh'
          }
        }
        stage('test 6.1.0 on centos7') {
          environment {
            OS = 'centos7'
            VERSION = '6.1.0'
          }
          agent { label "centos7" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './check-build.sh'
          }
        }
        stage('test 6.1.2 on ubuntu 1404') {
          environment {
            OS = 'u1404'
            VERSION = '6.1.2'
          }
          agent { label "u1404" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './check-build.sh'
          }
        }
        stage('test 6.1.0 on ubuntu 1404') {
          environment {
            OS = 'u1404'
            VERSION = '6.1.0'
          }
          agent { label "u1404" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './check-build.sh'
          }
        }
        stage('test 6.1.2 on ubuntu 1610') {
          environment {
            OS = 'centos6'
            VERSION = '6.1.2'
          }
          agent { label "u1610" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './check-build.sh'
          }
        }
        stage('test 6.1.0 on ubuntu 1610') {
          environment {
            OS = 'u1610'
            VERSION = '6.1.0'
          }
          agent { label "u1610" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './check-build.sh'
          } // steps
        } // stage
      } // parallel
    } // stage test
  } // stages
  post {
    always {
      echo 'One way or another, I have finished'
      deleteDir() /* clean up our workspace */
      archiveArtifacts artifacts: '$WORKSPACE/build-$BUILD_NUMBER/*', fingerprint: true
    }
    success {
      slackSend channel: '#gmp-code-rade',
      color: 'good',
      message: "The pipeline ${currentBuild.fullDisplayName} completed successfully."
    }
    failure {
      slackSend channel: '#gmp-code-rade',
      color: 'bad',
      message: "The pipeline ${currentBuild.fullDisplayName} completed successfully."
    }
  }
}