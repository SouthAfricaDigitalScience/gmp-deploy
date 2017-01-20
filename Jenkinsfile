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
