pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "mern-ci-app"
    }

    stages {
        stage('Build & Run Docker Containers') {
            steps {
                sh 'docker compose -p $COMPOSE_PROJECT_NAME -f docker-compose.yml up -d --build'

            }
        }
    }
}
