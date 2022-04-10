pipeline {
    agent any

    stages{

        stage('Clone Repository'){
            /* Cloning the repository to my workspace*/
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps{
                sh 'sudo docker build -t flaskblog:v1 . '
            }
        }

        stage('Run Image') {
            steps{
                sh 'sudo docker run -p 5000:5000 -d --name flaskblog flaskblog:v1'
            }
        }

        stage ('Unittests') {
            steps {
                sh 'python3 test_routes.py'
            }
            post {
                always {junit 'test-reports/*.xml'}
            }
        }

        stage ('GUI-Test') {
            steps {
                sh 'echo This is where the GUI-Test was supposed to take place' 
            }
        }
    }
}
                