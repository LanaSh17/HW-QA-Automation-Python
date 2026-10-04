pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install -r requirements.txt'
                sh '.venv/bin/python -m playwright install'
            }
        }

        stage('Run tests') {
            steps {
                sh '.venv/bin/python -m pytest --junitxml=test-results.xml'
            }
        }

        stage('Publish test results') {
            steps {
                junit 'test-results.xml'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }

        success {
            echo 'Tests passed successfully'
        }

        failure {
            echo 'Tests failed'
        }
    }
}