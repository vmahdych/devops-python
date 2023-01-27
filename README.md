# The main goal of the project is to create a CI/CD pipeline to AKS for python webapp.


## Following instruments are used:

- Git based:
  - Git - as a version control system;
  - GitHub - a cloud-based Git repository hosting service;
  - GitHub Actions - as a tool to create and maintain the CI/CD process;
- Container based:
  - Docker - to generate an image;
  - Kubernetes - as a container orchestration platform;
  - Helm - as a Kubernetes-based deployment tool for automating the creation, packaging, configuration, and deployment of the app;
- Azure cloud hosting with the following instances:
  - ACR - to store images;
  - AKS - to deploy the app;
  - Azure DNS Zone;
  - Azure File Storage;
 

## To-Do List

- [x] Task 1: Create containerized app along with Dockerfile, K8s manifests and Helm charts;
- [x] Task 2: Create all the required Azure instances;
- [x] Task 3: Configure GitHub;
- [x] Task 4: Create two wokrflow files: staging and production;
- [x] Task 5: Add upload functional as well as Storage for files;
- [x] Task 6: Istall SSL;

### Task 1
- [x] Create Flask webapp;
- [x] Create Dockerfile;
- [x] Build Docker image;
- [x] Create deployment and service Kubernetes manifests files;
- [x] Add Helm to the game and convert manifests accordingly;
- [x] Run app locally to make sure everything work as should.

### Task 2
- [x] Create init.sh script to create all the required instances;
- [x] Check all the instances;

### Task 3
- [x] Create PAT if you do not have one;
- [x] Add all the required secrets (check workflow files from task 4);

### Task 4
- [x] Create base staging workflow;
- [x] Create base production workflow;
- [x] Push changes to GitHub to make sure workflows are running.

### Task 5
- [x] Create of find suitable app functionsl;
- [x] Create PV and PVC for namespaces;
- [x] Push and check.

### Task 6
- [x] Create an ingress controller;
- [x] Create cert manager;
- [x] Update appropriate DNS records;
- [x] Create and run Cluster issues using Let`s Encrypt SSL;
- [x] Update ingress if needed.


## Things that can be implemented / improved:
- Role Based Access Control
- Livenes Probe
- Improve images security
