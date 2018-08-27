pipeline{
    triggers {
        githubPush
    }
    agent {
        label 'x86 centos6'
    }
    environment {
    OS = "sl6"
    SITE = "generic"
    ARCH = "x86_64"
    NAME = "gmp"
    VERSION = "6.1.2"
    }

    node { // <1>
    
        stage('Build') { // <2>
            sh 'build.sh' // <3>
        }

        stage('Test') { // <4>
            sh 'check-build.sh'
        }
        stage('Deploy') {
            sh 'build.sh'
        }
    }
}
