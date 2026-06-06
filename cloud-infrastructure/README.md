# AWS Cloud Infrastructure via Terraform (IaC)

## 📋 Overview
This directory houses the Infrastructure as Code (IaC) templates used to programmatically provision and manage high-availability cloud infrastructure on Amazon Web Services (AWS). Using code to define resources ensures deployments are repeatable, version-controlled, and free from human error during configuration.

## 🏗️ Architecture Blueprint
The configuration file (`main.tf`) spins up a foundational, secure public-facing cloud tier utilizing the following elements:
* **Virtual Private Cloud (VPC):** An isolated logical network partition (`10.0.0.0/16`) inside the AWS global footprint.
* **Public Subnet:** A segmented block (`10.0.1.0/24`) inside an explicit Availability Zone mapped to route external traffic.
* **Internet Gateway (IGW) & Route Tables:** Establishes the edge routing mechanisms required to connect the VPC securely to the public internet.
* **Security Group Firewall:** Enforces strict stateful ingress control parameters allowing restricted entry exclusively on ports `22` (SSH management) and `80` (HTTP standard traffic).
* **EC2 Instance Compute Tier:** Provisions a virtualized compute platform running Ubuntu Server LTS, integrated directly into the secured subnet architecture.

## 🛠️ Deployment Instructions
To initialize and test this environment locally:
1. Ensure your local machine has the Terraform CLI and AWS CLI authenticated.
2. Initialize the backend tracking provider context:
   ```bash
   terraform init