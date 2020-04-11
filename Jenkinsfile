pipeline{
    agent any
	environment
	{
		build = "${env.BUILD_NUMBER}"
	}
	stages{
		stage("Update git repository") {
			steps{sh '''
                sudo su - jenkins
                cd PracticalProject
                git checkout development-test
                git pull
                echo "${build}"
                '''
			}
		}
		stage("Build") {
			steps{sh '''
                sudo su - jenkins
                cd PracticalProject
                export BUILD_NUMBER="${build}"
                docker-compose build
                docker-compose push
                '''
			}
		}
		stage("Deploy") {
			steps{sh '''ssh ansible-app << EOF
                sudo su - jenkins
                cd PracticalProject
                git pull
                export BUILD_NUMBER="${build}"
                #scp ./nginx/nginx.conf
                docker stack deploy --compose-file docker-compose.yaml stack
                '''
			}
		}
	}
}