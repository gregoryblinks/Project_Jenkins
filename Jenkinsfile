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

        stage ('Test') {
            steps {
                sh 'python3 test_routes.py'
                sh 'python3 test_gui.py '
            }
            post {
                always {junit 'test-reports/*.xml'}
            }
        }

        stage ('Run App Necessities') {
            steps {
                sh 'pip install selenium' 
            }
        }
    }
}
                