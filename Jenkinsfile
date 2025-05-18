pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "mern-ci-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Laiba-Sami/resturant.git'
            }
        }

        stage('Build & Run Docker Containers') {
            steps {
                sh 'docker-compose -p $COMPOSE_PROJECT_NAME -f docker-compose.yml up -d --build'
            }
        }
    }
}
