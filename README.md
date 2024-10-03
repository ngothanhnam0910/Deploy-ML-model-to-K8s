# Build machine learning app with FastAPI: Dockerize and deploy to Kubenetes

## Feature

- Predict the nationality of individuals using their names
- Dockerizing FastAPI application
- Deploy the FastAPI application to Kubernetes cluster using minikube

## Prerequisites
- Docker installed in machine :  ```https://docs.docker.com/engine/install/ubuntu/```
- Minikube installed in machine: ```https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download```

## Installation

Clone the repository: ``` https://github.com/ngothanhnam0910/Deploy-ML-model-with-K8s.git ```

Install the libraries listed in the ```requirements.txt``` file if you want to analyze the data and train the model written in the ```data_analysis.ipynb``` file.

## Usage
**Explain the components**

- The ```app.py``` file is the main file that runs the FastAPI application.
- The ```deployment.yaml``` file is the configuration file for the Deployment and Service used to deploy the application on Kubernetes.
- The ```helm/``` directory contains the Helm chart used for deploying the application on Kubernetes. This chart includes all the necessary Kubernetes manifests and allows for easy customization and management of the application's deployment.

There are two ways to deploy the application to Kubernetes:
- Method 1: Run the command ```kubectl apply -f deployment.yaml```
- Method 2: Using Helm ```cd helm/fastapi-app && helm upgrade --install fastapi-app .```

## Check application
- Check ip minikube: ```minicube ip```
- Access address:  ```http://minicube_ip:32000/docs``` if using method 1 or ```http://minicube_ip:32001/docs```
