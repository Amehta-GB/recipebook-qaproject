pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                echo 'Hello World'
                
                sh "cd test_app_folder"
                

            }
        }
        
        stage('Build') {
            steps {
                
                
                
                sh "rm -rf recipebook-qaproject"
                sh "cd ."
                sh "rm -rf test_app_folder"
                

                
               
            }
        }
        
        
        
    }
}
