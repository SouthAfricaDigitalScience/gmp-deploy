pipeline {
  agent none
  environment {
    ARCH    = 'x86_64'
    SITE    = 'generic'
    NAME    = 'gmp'
    SRC_URL = 'https://gmplib.org/download/gmp/'
  }
  stages {
    stage('cache tarball') {
      parallel {
        stage ('6.1.2') {
          options { retry(3) }
          environment {
            VERSION   = '6.1.2'
            SRC_FILE  = "${env.NAME + '-' + env.VERSION + '.tar.bz2'}"
            SRC_DIR   = "${'/data/src/' + env.NAME }"
          }
          agent { label 'centos7' }
          steps {
            sh 'mkdir -vp ${SRC_DIR}'
            script {
              if(!fileExists("${SRC_DIR}/${SRC_FILE}")  && !fileExists("${SRC_DIR}/${SRC_FILE}.lock")) {
                echo "${SRC_DIR}/${SRC_FILE} not present"
                touch "${SRC_DIR}/${SRC_FILE}.lock"
                sh 'wget ${SRC_URL}/${SRC_FILE} -O ${SRC_DIR}/${SRC_FILE}'
                sh 'rm ${SRC_DIR}/${SRC_FILE}.lock' 
              }     
              else if(fileExists("${SRC_DIR}/${SRC_FILE}.lock"))
                while (!fileExists("${SRC_DIR}/${SRC_FILE}.lock")) {
                  sh 'file busy downloading there'
                }
              else {
                echo "file is already there"
              }
            }
          }
        }
        stage ('6.1.0') {
          environment {
            VERSION='6.1.0'
            SRC_FILE="${env.NAME + '-' + env.VERSION + '.tar.bz2'}"
            SRC_DIR = "${'/data/src/' + env.NAME }"
          }
          agent { label 'centos7' }
          steps {
            sh 'mkdir -vp $SRC_DIR'
            sh 'wget ${SRC_URL}/${SRC_FILE} -O ${SRC_DIR}/${SRC_FILE}'
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
          options { 
            retry(3) 
            skipDefaultCheckout() 
          }
          agent { label 'centos6' }
          steps {
            sh 'pwd'
            sh 'echo $SITE $NAME $OS $ARCH $VERSION $WORKSPACE'
            sh './build.sh'
            sh ''
          }
        }
        stage('build 6.1.0 on centos6') {
          environment {
            OS = 'centos6'
            VERSION = '6.1.0'
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
          }
          agent { label "u1404" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './build.sh'
          }
        }
        stage('build 6.1.2 on ubuntu 1610') {
          environment {
            OS = 'u1610'
            VERSION = '6.1.2'
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
          }
          agent { label "u1404" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './check-build.sh'
          }
        }
        stage('test 6.1.2 on ubuntu 1610') {
          environment {
            OS = 'u1610'
            VERSION = '6.1.2'
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
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
            WORKSPACE = "${'/home/jenkins/workspace/' + env.NAME + '/' + env.VERSION + '/' + env.OS}"
          }
          options { 
            retry(3) 
            skipDefaultCheckout() 
          }
          agent { label "u1610" }
          steps {
            sh 'echo $SITE $NAME $OS $ARCH $VERSION'
            sh './check-build.sh'
          } // steps
        } // stage
      } // parallel
    } // stage test
    stage('ship') {
      parallel {
        stage('ship 6.1.0') {
           environment {
            VERSION = '6.1.0'
            TARBALL = "${env.NAME} + \
                      '-' + ${env.VERSION} + \
                      '-' + ${env.SITE} + \
                      '-' + ${ARCH} + \
                      '-' + ${env.OS}.tar.gz" // ${env.BUILD_NUMBER}.tar.gz"
            ZENODO_API_KEY = credentials('zenodo_access_token')
           }
           options { 
            retry(3) 
            skipDefaultCheckout() 
          }
           agent { label "centos7"}
           steps {
             sh "tar cvfz ${TARBALL} /data/ci-build/generic/${OS}/${ARCH}/${NAME}/${VERSION}"
             sh "python publish.py"
           }
        }
      }
    }
  } // stages
  post {
    always {
      agent { label 'centos7' }
      echo 'One way or another, I have finished'
      archiveArtifacts artifacts: '$WORKSPACE/build-$BUILD_NUMBER/*', fingerprint: true
      deleteDir()
    }
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
  }
}