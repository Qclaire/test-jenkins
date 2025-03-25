@Library('my-shared-library') _
pipeline {
    agent any
    stages {
        stage('Get Commit Info') {
            steps {
                script {
                    def commitInfo = getCommitInfo()
                    echo "Commit Hash: ${commitInfo.hash}"
                    echo "Author: ${commitInfo.author}"
                    echo "Message: ${commitInfo.message}"
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    buildDockerImage('cool-python-app:latest', [BUILD_VERSION: '1.0'])
                }
            }
        }
        stage('Security Scan') {
            steps {
                script {
                    def scanResult = securityScan('sonarqube')
                    if (!scanResult) {
                        error "Security scan failed!"
                    } else {
                        echo "Security scan passed!"
                    }
                }
            }
        }
    }
}
