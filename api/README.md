# Customer Order Management System

## Overview

This project is a Customer Order Management System built using Django and PostgreSQL. It allows users to input or select customers from a list and choose items from a dropdown list to submit an order along with relevant quantity.The amount is calculated automatically and the user is redirected to a success page. Additionally, it integrates Africa's Talking API to send customers a response once their order is successfully submitted. The system is deployed on Amazon Web Services (AWS) using CodeDeploy for Continuous Integration/Continuous Deployment (CI/CD) pipeline

## Features

- **Customer Management:** Users can add customers to the system.
- **Order Submission:** Users can select a customer, choose items from a dropdown list, quantity and submit an order.
- **Price Calculation:** Prices are automatically calculated based on the selected items.
- **Integration with Africa's Talking:** Sends customers a response message once the order is successfully submitted.
- **Google OAuth Authentication:** Utilizes Google OAuth for user authentication and authorization.

## Technologies Used

- Django: Python web framework for building the application.
- PostgreSQL: Database management system for storing customer and order data.
- Amazon Web Services (AWS): Cloud platform used for deployment.
- CodeDeploy: CI/CD tool for automating the deployment process.
- Africa's Talking API: Integration for sending response messages to customers.
- Google OAuth: Authentication mechanism for user login and access control.

## Installation

1. Clone the repository:

   
   git clone https://github.com/mahuthu/informatics.git

2. Navigate to the project directory:

Copy code
cd api

3. Install dependencies:
bash

pip install -r requirements.txt


4. Set up the PostgreSQL database and configure the database settings in settings.py 

5. Set up Google OAuth credentials and configure authentication settings.

6 Set uo Africas talking credentials and configure authentication settings. this is the username, api key and the sender id.

6. Run migrations:

    python manage.py makemigrations

    python manage.py migrate

7. Start the development server:
    python manage.py runserver

Access the application at http://localhost:8000.

superuser - jona
password - mahuthu8108

## Deployment
1. Set up an AWS account and configure AWS credentials on your machine.


2. Create an IAM role with necessary permissions for CodeDeploy.

3. Install AWS CLI and configure it with your AWS credentials.

4. Create a CodeDeploy application and deployment group.

5. Configure the scripts, buildspec.yml, appspec.yml file for CodeDeploy         deployment.

6. Push your changes to the AWS CodeCommit repository.

7. AWS CodePipeline will trigger the CI/CD pipeline, deploying the application to an EC2 instance.

## Usage
- Open the application in your web browser.

- Navigate to the Customer Management section to add customers.

- Go to the Order Submission page to select a customer, choose items, Quantity and submit an order.

- After submission, Africa's Talking will send a response message to the customer confirming the order.

- Contributing
Contributions are welcome! If you have suggestions, enhancements, or bug fixes, please fork the repository and submit a pull request.

**shareable links:** http://ec2-18-130-110-248.eu-west-2.compute.amazonaws.com

                    https://informatics-j7hq.onrender.com