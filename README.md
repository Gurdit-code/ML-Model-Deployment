# House price prediction API
A machine learning API for predicting house prices using FastAPI.

## Technologies
- python 
- pandas
- scikit-learn
- FastAPI
- docker 
- Joblib

## installation 
- pip install -r requirements.txt

## run the API
 uvicorn app:app --reload
 then api will available at http://127.0.0.1:8000 then go to documentation by /docs

## run the app 
- streamlit run app.py

## Project Files
train.py
Used to train the Machine Learning model using the house price dataset.

app.py
Contains the FastAPI application and prediction endpoint.

main.py
Contains the main application/API logic used by the project.

data/
Contains the dataset used for training the Machine Learning model.

model/
Contains the trained Machine Learning model saved as a .pkl file.

Dockerfile
Contains instructions for building the Docker image.

docker-compose.yml
Contains the Docker Compose configuration used to build and run the application.

.dockerignore

Specifies files that should not be included in the Docker build context.

## Docker   this project also be run using docker.

- make sure docker is installed and runnin

- build docker images
docker build -t house-price-api.

- run docker container
docker run -p 8000:8000 house-price-api
The api will be available at    http://localhost:8000

- build and start
docker compose up --build

- run in backround
docker compose up -d

- check running containers
docker ps

- view logs
docker compose logs

- Stop the application
docker comose down

## docker workflow

Application Source Code
        |
        v
    Dockerfile
        |
        v
   Docker Image
        |
        v
 Docker Container
        |
        v
 FastAPI Application
        |
        v
 Machine Learning Model
        |
        v
 Prediction Response

 ## install them using 
 pip install -r requirements.txt

Auther 

Gurditta 