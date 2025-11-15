pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "amantrivedi09/flask-cicd-k8s"
  }

  stages {

    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/raja0903/flask-cicd-k8s.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${DOCKER_IMAGE}:latest ."
      }
    }

    stage('Login & Push to DockerHub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USR', passwordVariable: 'PWD')]) {
          sh "echo $PWD | docker login -u $USR --password-stdin"
          sh "docker push ${DOCKER_IMAGE}:latest"
        }
      }
    }
  }

  post {
    success {
      echo "🎉 Docker Image Pushed Successfully! Next: kubectl apply -f k8s/"
    }
    failure {
      echo "❌ Build/Push Failed. Check Jenkins logs."
    }
  }
}

