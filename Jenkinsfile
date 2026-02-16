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
                sh 'sudo apt-get update || echo "Update skipped - no sudo access"'
            }
        }

        stage('Clone repo'){
            steps{
                git branch: 'master', url: 'https://github.com/kingpin1374/webpage.git', credentialsId: 'github'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:latest .'
            }
        }
        
        stage('Deploy with docker compose'){
            steps{
                // Stop and remove all related containers
                sh 'docker compose down -v --remove-orphans || true'
                sh 'docker stop $(docker ps -q --filter "name=flask") || true'
                sh 'docker rm $(docker ps -aq --filter "name=flask") || true'
                // Start app, rebuilding flask image with port 6000
                sh 'docker compose up -d --build --force-recreate'
                // Verify port mapping
                sh 'docker ps | grep flask-app || echo "Container not found"'
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
