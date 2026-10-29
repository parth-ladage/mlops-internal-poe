pipeline {
    agent any

    stages {
        stage('Chekcout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install pytest
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '.venv/bin/python hello.py'
            }
        }
    }
}