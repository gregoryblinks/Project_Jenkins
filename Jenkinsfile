pipeline {
//None parameter in the agent section means that no global agent will be allocated for the entire Pipeline’s
//execution and that each stage directive must specify its own agent section.
    agent any

    stages{
        stage('Build') {
            steps {
                sh 'pip3 install --user flask'
                sh 'pip3 install --user pytest'
                sh 'pip3 install --user flask_sqlalchemy'
                sh 'pip3 install --user flask_bcrypt'
                sh 'pip3 install --user flask_login'
                }
            }
        stage ('Test') {
            steps {
                sh 'python3 test_routes.py'
            }
            post{
                always {juni 'test-reports/*.xml'}
            }
        }
    }
}
                