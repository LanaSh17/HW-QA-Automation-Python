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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest --junitxml=test-results.xml'
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