# Day 12 – REST APIs & Python Requests for Cloud Security

## 📅 Date

03 July 2026

---

# 🎯 Objective

Today's goal was to understand how Python communicates with cloud services using REST APIs. Since AWS, Azure, and most security platforms expose REST APIs, this knowledge forms the foundation of cloud security automation.

---

# 📚 Topics Covered

## 1. REST APIs

### What I Learned

- REST (Representational State Transfer)
- API communication model
- Endpoints
- Request and Response
- Headers
- Request Body
- JSON Response

---

## 2. HTTP Methods

| Method | Purpose |
|---------|---------|
| GET | Retrieve data |
| POST | Create new resource |
| PUT | Update existing resource |
| DELETE | Remove resource |

---

## 3. HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Resource Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## 4. Python Requests Library

### Learned

- Installing Requests

```bash
pip install requests
```

- Sending GET requests
- Processing JSON responses
- Checking HTTP Status Codes
- Exception Handling for API requests

---

# 🛠 Project Built

## Public API Security Dashboard

### Features

- Connects to GitHub Public REST API
- Sends HTTP GET requests
- Reads JSON responses
- Displays important API information
- Validates Status Codes
- Handles Connection Errors

---

# ☁ Cloud Security Connection

REST APIs are used by:

- AWS
- Microsoft Azure
- Google Cloud
- Microsoft Graph
- GitHub
- VirusTotal
- CrowdStrike
- Splunk
- ServiceNow

Understanding REST APIs is essential before learning:

- AWS Boto3
- Azure SDK
- Security Automation
- Cloud Incident Response
- DevSecOps

---

# 📈 Learning Workflow

Python Script

↓

Requests Library

↓

REST API

↓

JSON Response

↓

Python Dictionary

↓

Process Data

↓

Automation

---

# 💡 Key Takeaways

- REST APIs are the standard way cloud services communicate.
- Python uses the Requests library to interact with APIs.
- JSON is the most common response format.
- Always validate HTTP Status Codes.
- API communication is the foundation of cloud automation.

---

# 🚀 Next Goal

- API Authentication
- Environment Variables
- AWS Boto3
- Azure SDK
- Cloud Security Automation

---

# 📚 Skills Learned So Far

### AWS Cloud Security Foundation ✅

- IAM
- EC2
- S3
- VPC
- CloudTrail
- CloudWatch
- AWS Config
- GuardDuty
- Amazon Inspector
- Security Hub

---

### Python for Cloud Security 🚀

- JSON
- File Handling
- CSV Processing
- Logging
- Exception Handling
- Requests Library
- REST APIs

---

# 🎯 Project Status

✅ Public API Security Dashboard Completed

Next Project:

➡ API Authentication
➡ AWS SDK (Boto3)
➡ IAM Security Auditor

---

# 💭 Personal Reflection

Today I learned that almost every cloud platform communicates through REST APIs. Understanding this workflow makes it much easier to understand how AWS SDKs, Azure SDKs, and cloud security automation tools work behind the scenes.