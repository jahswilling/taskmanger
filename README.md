# Task Manager App with CloudFormation and Ansible

## Overview

This project deploys a Task Manager application using Amazon Web Services (AWS) CloudFormation for infrastructure provisioning and Ansible for configuration management. The app is designed to help users manage their tasks and to-dos efficiently. Additionally, GitHub Actions are used for automated deployment and continuous integration.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Deployment](#deployment)
- [Accessing the App](#accessing-the-app)
- [Customizing the App](#customizing-the-app)
- [GitHub Actions Workflow](#github-actions-workflow)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project consists of the following components:

- **CloudFormation Templates:** These are used to define the AWS infrastructure required for the app.

- **Ansible Playbooks:** Ansible playbooks define how the app should be configured on the EC2 instance.

- **Django Task Manager App:** The actual task management application developed using Django.

- **GitHub Actions Workflow:** Automated deployment and continuous integration workflows for the project.

- **README and Documentation:** Project documentation and this README.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- AWS account with necessary permissions.
- AWS CLI installed and configured with your AWS credentials.
- Ansible installed on your local machine.
- A GitHub repository for your project.

## Deployment

1. Clone this repository to your local machine.

2. Navigate to the `cloudformation` directory and deploy the CloudFormation stack using the AWS CLI:

   ```bash
   aws cloudformation deploy --stack-name TaskManagerStack --template-file cloudformation.yaml --capabilities CAPABILITY_NAMED_IAM
