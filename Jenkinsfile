pipeline {
    agent any



        




    stages {



        stage('Preparation') {
            steps {
                echo 'Hello World'
                sh "mkdir test_app_folder"
                sh "cd test_app_folder"
                sh "git clone https://github.com/Amehta-GB/recipebook-qaproject.git"
                sh "cd recipebook-qaproject"
                sh "export DATABASE_URI=sqlite:/// CREATE_SCHEMA=true"
                
                
                


            }
        }

        stage('Test') {
            steps {

                echo 'Hello World'


            }
        }

        
        stage('cleanup') {
            steps {
                sh "cd ."
                sh "rm -rf recipebook-qaproject"
                sh "cd ."
                sh "rm -rf test_app_folder"
                 
            }
        }
        
        
        
    }
}
