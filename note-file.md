Instance/VM : Amazon Linux 

INSTALLATION 
Update the system : 
Command : sudo yum update
git installation
Command : sudo yum install git -y

Clone github repository

Command : git clone <git_link>

Installation of EKSCTL
=========================================================================================================================================
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version

Kubectl installation
==============================================================================================================================
sudo yum install kubectl -y 
curl -LO "https://cdn.dl.k8s.io/release/$(curl -L -s https://cdn.dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -LO "https://cdn.dl.k8s.io/release/$(curl -L -s https://cdn.dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
chmod +x kubectl
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
kubectl 
==============================================================================================================================

Cluster Creation
==============================================================================================================================
eksctl create cluster --name simple-django-app --region ap-south-1 --node-type t3.medium --nodes-min 2 --nodes-max 2
aws eks update-kubeconfig --region ap-south-1 --name simple-django-app 
kubectl get nodes

go to the cloned directory : 
Command : cd simple-django-app
command : cd kubernetes
Command: kubectl apply -f deployment.yaml
Command : kubectl apply -f service.yaml
Command : kubectl get services
o/p : 
[ec2-user@ip-172-31-2-224 kubernetes]$ kubectl get svc 
NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP                                                              PORT(S)          AGE
kubernetes                  ClusterIP      10.100.0.1      <none>                                                                   443/TCP          14m
simple-django-app-service   LoadBalancer   10.100.246.17   ad3f1e6fb1e714a939e7a3ddb8f873dc-90838841.ap-south-1.elb.amazonaws.com   8000:32004/TCP   6m36s

================================================================================================================================

GO TO THE BROWSER
================================================================================================================================
write this url and search : 

http://ad3f1e6fb1e714a939e7a3ddb8f873dc-90838841.ap-south-1.elb.amazonaws.com:8000


