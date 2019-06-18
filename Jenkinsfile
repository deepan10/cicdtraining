pipeline {
    agent any
    stages {
        stage ("setup") {
            steps {
                script {
                    if(isUnix()) {
                        sh '''
                            pip install virtualenv
                            virtualenv .venv
                            source .venv/bin/activate
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            pip install virtualenv
                            virtualenv .venv
                            .venv/Script/activate
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        stage ("Build") {
            steps {
                sh 'echo hi'
            }
        }
        stage ("Testing") {
            parallel {
                stage ("Unittest") {
                    steps {
                        sh '''
                            source .venv/bin/activate
                            pytest --cov=src --cov-report=html tests/
                        '''
                    }
                }
                stage ("Lint check") {
                    steps {
                        sh '#pylint src/ tests/'
                    }
                }
            }
        }
        stage ("Deploy local") {
            steps {
                sh '''
                    source .venv/bin/activate
                    which python
                    python setup.py install
                '''
            }
        }
        stage ("Integration Test") {
            steps {
                sh '''
                    source .venv/bin/activate
                    robot integrationtests/test_app_calc.robot
                '''
            }
        }
        stage ("Deploy Prod") {
            steps {
                sh 'echo deploy'
            }
        }
    }
}