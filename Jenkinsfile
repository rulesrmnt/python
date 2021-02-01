pipeline {
    agent any

    stages {
        stage('Git-Checkout') {
            steps {
                echo 'Git repo'
                git 'https://github.com/rulesrmnt/python.git'
            }
        }
        stage('build') {
            steps {
                echo 'tuple_example'
                bat 'python tuple_example.py'
            }
        }
        
        stage('print hello world'){
            steps {
                echo 'print hello '
                bat 'python hello_world.py'
            }
        }
        
    }
}
