pipeline {
  agent {
    docker {
      image 'quay.io/aaroc/code-rade-centos6:latest'
    }

  }
  stages {
    stage('sanity') {
      parallel {
        stage('sanity centos6') {
          agent {
            docker {
              image 'quay.io/aaroc/code-rade-centos7'
            }

          }
          environment {
            HOME = '/home/jenkins/'
          }
          steps {
            node(label: 'centos6') {
              echo 'node allocated'
              fileExists 'build.sh'
              fileExists 'check-build.sh'
              fileExists 'deploy.sh'
            }

          }
        }
        stage('sanity centos7') {
          agent {
            docker {
              image 'quay.io/aaroc/code-rade-centos7'
            }

          }
          environment {
            HOME = '/home/jenkins'
          }
          steps {
            fileExists 'build.sh'
            node(label: 'centos7')
          }
        }
      }
    }
    stage('build') {
      parallel {
        stage('build centos6') {
          agent {
            node {
              label 'centos6'
            }

          }
          environment {
            HOME = '/home/jenkins/'
          }
          steps {
            sh './build.sh'
          }
        }
        stage('build centos7') {
          agent {
            node {
              label 'centos7'
            }

          }
          steps {
            sh './build.sh'
          }
        }
      }
    }
    stage('test') {
      steps {
        sh './check-build.sh'
      }
    }
  }
  environment {
    HOME = '/home/jenkins'
  }
}