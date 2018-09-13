pipeline {
  agent none
  environment {
    ARCH = 'x86_64'
    SITE = 'generic'
    NAME = 'gmp'
  }
  stages {
    stage('cache tarball') {
      parallel {
        stage ('6.1.2') {
          environment {
            VERSION='6.1.2'
            SOURCE_FILE="${env.NAME + '-' + env.VERSION + '.tar.bz2'}"
            SRC_DIR = "${'/data/src/' + env.NAME }"
          }
          agent { label 'centos7' }
          steps {
            sh 'mkdir -vp $SRC_DIR'
            sh 'wget $SOURCE_FILE -O $SRC_DIR'
          }
        }
        stage ('6.1.0') {
          environment {
            VERSION='6.1.0'
            SOURCE_FILE="${env.NAME + '-' + env.VERSION + '.tar.bz2'}"
            SRC_DIR = "${'/data/src/' + env.NAME }"
          }
          agent { label 'centos7' }
          steps {
            sh 'mkdir -vp $SRC_DIR'
            sh 'wget $SOURCE_FILE -O $SRC_DIR'
          }
        }
      }
    }
    stage('build') {
      parallel {
        stage('build 6.1.2 on centos6') {
          environment {
            OS = 'centos6'
            VERSION = '6.1.2'
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          agent { label 'centos6' }
          steps {
            sh 'pwd'
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './build.sh'
            sh ''
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
  // post {
  //   always {
  //     echo 'One way or another, I have finished'
  //     deleteDir() /* clean up our workspace */
  //     archiveArtifacts artifacts: '$WORKSPACE/build-$BUILD_NUMBER/*', fingerprint: true
  //   }
  //   success {
  //     slackSend channel: '#gmp-code-rade',
  //     color: 'good',
  //     message: "The pipeline ${currentBuild.fullDisplayName} completed successfully."
  //   }
  //   failure {
  //     slackSend channel: '#gmp-code-rade',
  //     color: 'bad',
  //     message: "The pipeline ${currentBuild.fullDisplayName} completed successfully."
  //   }
  // }
}