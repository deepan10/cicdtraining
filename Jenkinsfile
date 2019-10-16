pipeline {
    agent any
    stages {
        stage ("TEST") {
            when {
                anyOf { branch 'master'; branch 'feature/*' }
            }
            steps {
                echo "PASSED"
            }
        }
    }
}
