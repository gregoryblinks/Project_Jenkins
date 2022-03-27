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
                sh 'pwd'
                sh 'cd /var/lib/jenkins/workspace'
                sh 'pwd'
                sh ' docker build -t flaskblog:v1 .'
                sh 'pwd'
                sh 'docker-compose up' 
            }
        }

        stage('Build') {
            steps {
                sh 'pip3 install --user Flask==2.0.3'
                sh 'pip3 install --user pytest'
                sh 'pip3 install --user flask_sqlalchemy'
                sh 'pip3 install --user flask_bcrypt'
                sh 'pip3 install --user flask_login'
                sh 'pip3 install --user flask_mail'
                sh 'pip3 install --user flask_wtf'
                sh 'pip3 install --user itsdangerous==2.0.1'
                sh 'pip3 install --user email_validator'
                sh 'pip3 install --user pillow'
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
    }
}
                