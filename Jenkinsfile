pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\Ahmed Shaltout\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning the Django project...'
                git branch: 'main',
                    url: 'https://github.com/Ahmed-Shaltout3g/jenkins-python.git',
                    credentialsId: 'github-credentials'  // استخدم Credential ID اللي انت عامله في Jenkins
            }
        }

        stage('Set Up Python Environment') {
            steps {
                bat '''
                    "%PYTHON_PATH%" -m venv venv
                    call venv\\Scripts\\activate
                    "%PYTHON_PATH%" -m pip install --upgrade pip
                    "%PYTHON_PATH%" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    python manage.py makemigrations
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
