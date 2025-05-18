pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Laiba-Sami/resturant.git'
            }
        }

        stage('Build and Run with Docker Compose') {
            steps {
                script {
                    sh 'docker-compose -p resturant_ci -f docker-compose.yaml up -d --build'
                }
            }
        }
    }
}
