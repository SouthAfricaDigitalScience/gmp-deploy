pipeline{
    triggers {
        githubPush
    }
    environment {
    OS = "sl6"
    SITE = "generic"
    ARCH = "x86_64"
    NAME = "gmp"
    VERSION = "6.1.2"
    }

    stages { // <1>
        stage('CheckOut')
            scm CheckOut
        stage('Build') {
            agent {
               label 'x86 centos6'
            }
            sh 'build.sh' // <3>
        }
    }
}
