pipeline{
agent any 
  stages{
stage('one'){
  steps{
    echo"how are you doing,this is the start of project"
  }
}
    stage('two'){
      steps{
        input('Do you want to proceed?')
}
}
    stage('three'){
        when{
          not{
            branch 'main'
          }
        }
        steps{
          echo'till this you have come third stage'
        }
    }
    stage('four'){
      parallel{
        stage('Unit test'){
        steps{
          echo'Unit testing >>>>'
        }
        }
        stage('integration test'){
          steps{
            echo'integration testing is happening'
          }
        }
      }
    }
  }
}
        
          
