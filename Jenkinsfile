pipeline {
    agent {
        docker {
            label 'x86_64 sl6'
        }
    }
    environment {
    OS = "sl6"
    SITE = "generic"
    ARCH = "x86_64"
    NAME = "gmp"
    VERSION = "6.1.2"
    }

    stages {
        stage('build') {
            steps {
                sh 'build.sh'
            }
        }
        stage('test') {
            steps {
                sh 'check-build.sh'
            }
        }
        stage('deploy') {
            steps {
                sh 'deploy.sh'
            }
        }
    }
    post {
        always {
            echo "this step was run"
        }
    }
}
    
//     triggers {
//         github
//     }
//     stages { // <1>
//         stage('CheckOut')
//             scm CheckOut
//         stage('Build') {
//             agent {
//                label 'x86 centos6'
//             }
//             sh 'build.sh' // <3>
//         }
//     }
// }
