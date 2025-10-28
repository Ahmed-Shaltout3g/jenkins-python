pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the Django project...'
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                bat '''
    "C:\\Users\\Ahmed\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv
    call venv\\Scripts\\activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
'''
            }
        }

        stage('Run Migrations') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    python manage.py migrate
                '''
            }
        }

    
        stage('Run Django Server') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    python manage.py runserver 0.0.0.0:8000
                '''
            }
        }
    }
}
