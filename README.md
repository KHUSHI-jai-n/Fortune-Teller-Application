# Fortune Teller App

Fortune Teller is a simple web application that answers your questions with one of three possible responses: **Yes**, **No**, or **Maybe**. The app is hosted as a static website on Amazon S3 and integrates with an HTTP API built using AWS API Gateway and Lambda.

---

## Features

- **Interactive Frontend**: Built using HTML, CSS, and JavaScript.
- **Serverless Backend**: Utilizes AWS Lambda for the application logic and AWS API Gateway for API management.
- **Hosted on AWS S3**: Fully deployed as a static website for easy access.

---

## How It Works

1. **Ask a Question**: The user types a question into the input field on the webpage.
2. **API Invocation**: The frontend sends the question to an HTTP API hosted on AWS API Gateway.
3. **Backend Logic**: The API Gateway triggers an AWS Lambda function that processes the request and returns one of three responses: **Yes**, **No**, or **Maybe**.
4. **Display Response**: The response is displayed dynamically on the webpage.

---

## Technologies Used

### **Frontend**
- HTML
- CSS
- JavaScript

### **Backend**
- **AWS Lambda**: Contains the logic for generating random responses.
- **AWS API Gateway**: Serves as the HTTP interface for the backend.

### **Hosting**
- **Amazon S3**: Hosts the static files for the web application.

---

## Deployment

### Backend
1. **Lambda Function**:
   - The Lambda function is triggered by an HTTP API created in API Gateway.
  
2. **API Gateway**:
   - Configured to invoke the Lambda function.
   - CORS enabled to allow communication with the frontend.

### Frontend
1. **S3 Bucket**:
   - Static website hosting enabled.
   - Index document set to `fortuneTeller.html`.

2. **Bucket Policy**:
   - Public read access granted for the hosted files.
