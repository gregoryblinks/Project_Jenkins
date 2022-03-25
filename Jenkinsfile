pipeline {
//None parameter in the agent section means that no global agent will be allocated for the entire Pipeline’s
//execution and that each stage directive must specify its own agent section.
    agent { docker { image 'python:3.7.2'} }

    stages{
        stage('Build') {
            steps {
                sh 'pip install flask'
                }
            }
        stage ('Test') {
            steps {
                sh 'python test_routes.py'
            }
        }
    }
}
                