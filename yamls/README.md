# Deploy to Kubernetes

# Enable Ingress controller on Minikube

minikube addons enable ingress

## Create Kubernetes Resources

kubectl apply -f yamls/Deployment.yaml
kubectl apply -f yamls/Service.yaml
kubectl apply -f yamls/Ingress.yaml

## Add URL to HOSTS file
<Node-IP> ingress.rickandmorty.com