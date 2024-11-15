# Hello K8s - Déploiement de Flask et Nginx sur Kubernetes

Ce projet contient une application Flask servie via un reverse-proxy Nginx, déployée sur un cluster Kubernetes en utilisant Minikube.

## Prérequis

- [Docker](https://www.docker.com/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

## Structure du Projet

```
.
├── app.py                   # Application Flask
├── docker-compose.yml       # Fichier Docker Compose
├── Dockerfile               # Dockerfile pour Flask
├── nginx/
│   ├── Dockerfile           # Dockerfile pour Nginx
│   └── nginx.conf           # Configuration Nginx
├── requirements.txt         # Dépendances Python
└── k8s/
    ├── flask-deployment.yaml    # Déploiement Flask dans Kubernetes
    ├── flask-service.yaml       # Service pour Flask
    ├── nginx-deployment.yaml    # Déploiement Nginx dans Kubernetes
    └── nginx-service.yaml       # Service pour Nginx
```

## Déploiement

### Étapes pour déployer l'application

1. **Démarrer Minikube**
   ```bash
   minikube start
   ```

2. **Construire les images Docker et les charger dans Minikube**
   ```bash
   eval $(minikube -p minikube docker-env)
   docker build -t flask-app:latest .
   docker build -t nginx-app:latest ./nginx
   ```

3. **Appliquer les fichiers de déploiement Kubernetes**
   ```bash
   kubectl apply -f k8s/flask-deployment.yaml
   kubectl apply -f k8s/flask-service.yaml
   kubectl apply -f k8s/nginx-deployment.yaml
   kubectl apply -f k8s/nginx-service.yaml
   ```

4. **Vérifier l'état des Pods et Services**
   ```bash
   kubectl get pods
   kubectl get services
   ```

5. **Accéder à l'application via le service Nginx**
   Accédez à l'application sur l'adresse suivante, où `<MINIKUBE_IP>` est l'adresse IP de Minikube :
   ```
   http://<MINIKUBE_IP>:32100/
   ```

## Tester la haute disponibilité

Un script Python `load_test.py` est inclus pour tester la haute disponibilité et la scalabilité en envoyant plusieurs requêtes en parallèle.
