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
                "C:\\Users\\Ahmed Shaltout\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
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

        stage('Run Django Server in Background') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                start /B venv\\Scripts\\python.exe manage.py runserver 0.0.0.0:8000
                echo Django server started in background.
                '''
            }
        }

        stage('Pipeline Complete') {
            steps {
                echo 'Django app deployed successfully and pipeline finished!'
            }
        }
    }
}
