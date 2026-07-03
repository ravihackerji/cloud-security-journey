# Public API Security Dashboard using Python REST API

## 📌 Project Overview

This project demonstrates how Python communicates with web services using **REST APIs** and the **Requests** library.

The application sends an HTTP GET request to GitHub's public REST API, receives a JSON response, converts it into a Python dictionary, and displays useful API information.

This project introduces the same communication model used by AWS, Azure, Google Cloud, and other cloud platforms.

---

# 🎯 Objective

- Learn REST API fundamentals.
- Understand HTTP communication.
- Send GET requests using Python.
- Process JSON responses.
- Handle API errors.
- Build the foundation for AWS Boto3 and Azure SDK.

---

# 🛠 Technologies Used

- Python 3
- Requests Library
- REST API
- JSON

---

# 📂 Project Structure

```
Day-09-REST-API/
│
├── public_api_dashboard.py
├── README.md
├── interview_questions.md
└── sample_output.txt
```

---

# 🚀 Project Workflow

```
Python Script
      │
      ▼
Requests Library
      │
      ▼
HTTP GET Request
      │
      ▼
GitHub REST API
      │
      ▼
JSON Response
      │
      ▼
Python Dictionary
      │
      ▼
Display Information
```

---

# 📜 Features

- Sends HTTP GET requests.
- Connects to GitHub Public REST API.
- Checks HTTP Status Code.
- Converts JSON into Python Dictionary.
- Handles API connection errors.
- Demonstrates production-style API communication.

---

# 🌐 REST API Concepts

## Endpoint

```
https://api.github.com
```

---

## HTTP Method

```
GET
```

---

## Response Format

```
JSON
```

---

## Success Status Code

```
200 OK
```

---

# ▶ Expected Output

```
==================================================
GitHub Public API Dashboard
==================================================

Current User URL : https://api.github.com/user
Repository URL   : https://api.github.com/repos/{owner}/{repo}
Issues URL       : https://api.github.com/issues

Status Code      : 200
```

---

# ☁ Cloud Security Use Case

Cloud Security Engineers use REST APIs to communicate with:

- AWS Services
- Azure Services
- Google Cloud
- Microsoft Defender
- CrowdStrike
- Splunk
- VirusTotal
- GitHub
- ServiceNow

Nearly every cloud automation tool sends REST API requests behind the scenes.

---

# 🌍 Real-World Applications

- Cloud Resource Inventory
- Security Dashboard
- Threat Intelligence
- Vulnerability Management
- Incident Response
- IAM Automation
- Security Compliance
- SOC Automation

---

# 🚀 Future Improvements

- Add API Authentication.
- Read API Token from Environment Variables.
- Export Results to CSV.
- Save API Responses to JSON.
- Upload Reports to AWS S3.
- Send Notifications through Slack.
- Integrate with AWS Lambda.

---

# 📚 Key Concepts Learned

- REST API
- Endpoint
- HTTP Request
- HTTP Response
- GET Method
- Status Code
- JSON
- Requests Library

---

# 🎯 Learning Outcome

After completing this project, I can:

- Send HTTP requests.
- Read API responses.
- Process JSON data.
- Validate HTTP status codes.
- Build API-based automation.
- Prepare for AWS SDK (Boto3).

---

# 👨‍💻 Author

**Ravinder Verma**

B.Tech Information Technology

Aspiring Cloud Security Engineer

Learning AWS | Azure | Python | DevSecOps