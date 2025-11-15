pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "amantrivedi09/flask-cicd-k8s"
  }

  stages {

    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/raja0903/flask-cicd-k8s.git'
        script {
          env.COMMIT = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${DOCKER_IMAGE}:${COMMIT} -t ${DOCKER_IMAGE}:latest ."
      }
    }

    stage('Login & Push to DockerHub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USR', passwordVariable: 'PWD')]) {
          sh "echo $PWD | docker login -u $USR --password-stdin"
          sh "docker push ${DOCKER_IMAGE}:${COMMIT}"
          sh "docker push ${DOCKER_IMAGE}:latest"
        }
      }
    }

    stage('Deploy to Minikube') {
      steps {
        sh "kubectl set image deployment/flask-cicd-k8s flask-cicd-k8s=${DOCKER_IMAGE}:${COMMIT}"
        sh "kubectl rollout status deployment/flask-cicd-k8s"
      }
    }
  }

  post {
    success {
      echo "🎉 CI/CD Successful! Image tag: ${COMMIT}"
    }
  }
}

