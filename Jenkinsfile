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

                venv\\Scripts\\python.exe -m pip install --upgrade pip
                venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                venv\\Scripts\\python.exe manage.py migrate
                '''
            }
        }

        stage('Run Django Server') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                venv\\Scripts\\python.exe manage.py runserver 0.0.0.0:8000
                '''
            }
        }
    }
}
