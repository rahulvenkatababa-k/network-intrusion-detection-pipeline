### Network Security Projects For Phising Data

Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = 788614365622.dkr.ecr.us-east-1.amazonaws.com/networkssecurity
ECR_REPOSITORY_NAME = networkssecurity


Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker


1. Configure Setup.py
2. Configure Logging.py
3. Configure exception.py
4. tst_mongo_db.py
5. push_data.py
6. update schema.yaml
# follow stage by stage updaate data ingestion, data validation, model training, model evaluation steps 7->to->11 and update utils folder according to the requirement
7. __init__.py in constant\training_pipeline
8. config_entity.py 
9. configure artifact_entity.py file
10. create file with the satege in components folder
11. main.py
