pipeline {
//None parameter in the agent section means that no global agent will be allocated for the entire Pipeline’s
//execution and that each stage directive must specify its own agent section.
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
                sh 'sudo docker run -d -p 5000:4000 --name flaskblog flaskblog:v1'
            }
        }

        stage ('Test') {
            steps {
                sh 'python3 test_routes.py'
                sh 'python3 test_forms.py' 

            }
            post {
                always {junit 'test-reports/*.xml'}
            }
        }

        stage ('Run App') {
            steps {
                sh 'pip install requirements.txt'
                sh 'python3 run.py'
            }
    }
}
                