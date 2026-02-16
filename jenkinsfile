/* groovylint-disable-next-line CompileStatic */
pipeline {
    agent any
    
    environment {
        APP_NAME = 'webpage'
        APP_PORT = '6000'
        DOCKER_IMAGE = 'flask-app'
    }
    
    triggers {
        githubPush()
    }
    
    stages {
       stage ('Update') {
            steps {
                sh 'apt-get update'
            }
        }

        stage('Clone repo'){
            steps{
                git branch: 'master', url: 'https://github.com/kingpin1374/webpage.git'
                credentialsId: 'github'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:latest .'
            }
        }
        
        stage('Deploy with docker compose'){
            steps{
                // Stop existing container if they are running
                sh 'docker compose down || true'
                // Start app, rebuilding flask image
                sh 'docker compose up -d --build'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
            sh 'docker ps | grep ${DOCKER_IMAGE} || true'
        }
        failure {
            echo 'Pipeline failed!'
            sh 'docker logs ${DOCKER_IMAGE} || true'
        }
        always {
            echo 'Pipeline execution completed'
            sh 'docker system prune -f || true'
        }
    }
}
