pipeline {
    // Ändring 1
    // --------------------------
    // Bytte ut ursprungliga agent-raden mot detta:
    agent { label 'built-in' }
    // Det gör att Jenkins-jobbet kör på lokala datorn istället för i en docker container.
    // (Måste då vara noggran med att återställa miljön efter varje test-körning. Potentiellt kan det vara bra att lägga till en stage för det i Jenkins där man t.ex. tar bort alla filer i sitt Jenkins workspace inför nästa körning)
    // Detta fungerar också:
    // agent any
    // --------------------------
    stages {
        stage('build') {
            steps {
                // Ändring 2
                // ------------------------
                // Bytte ut "sh" mot "bat" eftersom min dator är en Windows. Detta behöver man inte göra om man använder Linux
                bat 'python --version'
                // ------------------------
            }
        }
    }
}