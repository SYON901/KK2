pipeline {
    // Ändring 1
    // --------------------------
    // Bytte ut ursprungliga agent-raden mot:
    agent any
    // --------------------------
    stages {
        stage('Testing gitHub-tests') {
            steps {
                // Ändring 2
                // ------------------------
                // Bytte ut "sh" mot "bat" eftersom min dator är en Windows. Detta behöver man inte göra om man använder Linux
                dir('C:/Users/samwi/gitEC/KK2/test_edge'){
                    bat 'pytest'
                }
            }
        }
        stage('Clean Workspace'){
            steps{
                cleanWs()
            }
        }
    }
}
