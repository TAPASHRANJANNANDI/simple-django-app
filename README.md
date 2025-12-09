# 🚀 Simple Django App Deployment on AWS EKS

This guide explains how to set up an **Amazon EKS Cluster on Amazon Linux**, install required tools, and deploy the **Simple Django Application** using Kubernetes.

---

## ✅ Prerequisites

* AWS Account
* EC2 Instance with **Amazon Linux**
* IAM Role attached with the following permissions:

  * AmazonEKSClusterPolicy
  * AmazonEKSWorkerNodePolicy
  * AmazonEC2ContainerRegistryReadOnly
  * AmazonEKSVPCResourceController

---

## 🖥️ Instance / VM Details

* **Operating System:** Amazon Linux

---

## 🔧 System Update & Git Installation

### 🔹 Update the system

```bash
sudo yum update -y
```

### 🔹 Install Git

```bash
sudo yum install git -y
```

---

## 📥 Clone GitHub Repository

```bash
git clone <git_link>
```

---

## ⚙️ Install eksctl

```bash
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
```

✅ This tool is used to create and manage EKS clusters.

---

## ☸️ Install kubectl

```bash
sudo yum install kubectl -y
```

OR (Manual Installation)

```bash
curl -LO "https://cdn.dl.k8s.io/release/$(curl -L -s https://cdn.dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -LO "https://cdn.dl.k8s.io/release/$(curl -L -s https://cdn.dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
chmod +x kubectl
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
```

---

## ☁️ EKS Cluster Creation

```bash
eksctl create cluster --name simple-django-app --region ap-south-1 --node-type t3.medium --nodes-min 2 --nodes-max 2
```

### 🔹 Update kubeconfig

```bash
aws eks update-kubeconfig --region ap-south-1 --name simple-django-app
```

### 🔹 Verify Nodes

```bash
kubectl get nodes
```

---

## 📂 Navigate to Kubernetes Directory

```bash
cd simple-django-app
cd kubernetes
```

---

## 🚀 Deploy Application to Kubernetes

### 🔹 Apply Deployment

```bash
kubectl apply -f deployment.yaml
```

### 🔹 Apply Service

```bash
kubectl apply -f service.yaml
```

### 🔹 Verify Services

```bash
kubectl get services
```

### ✅ Sample Output

```bash
NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP                                                              PORT(S)          AGE
kubernetes                  ClusterIP      10.100.0.1      <none>                                                                   443/TCP          14m
simple-django-app-service   LoadBalancer   10.100.246.17   ad3f1e6fb1e714a939e7a3ddb8f873dc-90838841.ap-south-1.elb.amazonaws.com   8000:32004/TCP   6m36s
```

---

## 🌐 Access Application on Browser

Open your browser and enter:

```text
http://ad3f1e6fb1e714a939e7a3ddb8f873dc-90838841.ap-south-1.elb.amazonaws.com:8000
```

✅ Your Django application should now be live!

---

## ✅ Summary

* ✅ EC2 Instance Setup
* ✅ EKS Cluster Created
* ✅ Django App Deployed
* ✅ LoadBalancer Exposed
* ✅ Application Accessible via Browser

---

## 📌 Notes

* Always ensure security groups allow port **8000**.
* Use **HPA & resource limits** for production scaling.
* Prefer **CI/CD pipelines** for automated deployment.

---

🎉 **Deployment Successfully Completed!**
