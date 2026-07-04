# Secure API Authentication Demo using Python

## 📌 Project Overview

This project demonstrates how authentication works when Python communicates with REST APIs.

It explains the difference between **Authentication** and **Authorization**, introduces API Keys, Bearer Tokens, OAuth, and demonstrates how authenticated API requests are made using Python's Requests library.

This project builds the foundation required for working with AWS SDK (Boto3), Azure SDK, Microsoft Graph API, GitHub API, and other cloud security APIs.

---

# 🎯 Objective

- Understand Authentication
- Understand Authorization
- Learn API Keys
- Learn Bearer Tokens
- Learn OAuth
- Send authenticated HTTP requests
- Understand secure API communication

---

# 🛠 Technologies Used

- Python 3
- Requests Library
- REST API
- HTTP Headers

---

# 📂 Project Structure

```
Day-10-Authentication/
│
├── api_auth_demo.py
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
Create HTTP Headers
      │
      ▼
Add Authentication Token
      │
      ▼
Send HTTP Request
      │
      ▼
REST API
      │
      ▼
Verify Identity
      │
      ▼
Check Permissions
      │
      ▼
Return Response
```

---

# 🔐 Authentication vs Authorization

## Authentication

Verifies **who you are**.

Example:

- Username & Password
- API Key
- Access Token

---

## Authorization

Determines **what you are allowed to access**.

Example:

- Read S3 Bucket
- Delete EC2 Instance
- Create IAM User

---

# 📜 Authentication Methods

## API Key

```
X-API-Key: YOUR_API_KEY
```

---

## Bearer Token

```
Authorization: Bearer YOUR_TOKEN
```

---

## OAuth

OAuth allows users to grant limited access without sharing their password.

Examples:

- Sign in with Google
- Sign in with GitHub
- Sign in with Microsoft

---

# ☁ Cloud Authentication Examples

## AWS

Uses:

- Access Key ID
- Secret Access Key
- IAM Roles

---

## Microsoft Azure

Uses:

- Microsoft Entra ID
- OAuth 2.0
- Service Principals
- Managed Identities

---

# ▶ Expected Output

```
Status Code: 200

Authentication request completed successfully.
```

---

# ☁ Cloud Security Use Cases

Authentication is used in:

- AWS SDK (Boto3)
- Azure SDK
- Microsoft Graph API
- GitHub API
- CrowdStrike API
- VirusTotal API
- Splunk API
- ServiceNow API

---

# 🌍 Real-World Applications

- IAM Automation
- Cloud Inventory
- Security Monitoring
- Compliance Reporting
- Incident Response
- Threat Intelligence
- DevSecOps Pipelines

---

# 🚀 Future Improvements

- Read API tokens from Environment Variables.
- Add Logging.
- Add Exception Handling.
- Connect to AWS using Boto3.
- Connect to Azure SDK.
- Generate Authentication Reports.

---

# 📚 Key Concepts Learned

- Authentication
- Authorization
- API Keys
- Bearer Tokens
- OAuth
- HTTP Headers
- Secure API Communication

---

# 🎯 Learning Outcome

After completing this project, I can:

- Explain Authentication and Authorization.
- Send authenticated API requests.
- Use HTTP headers correctly.
- Understand cloud authentication mechanisms.
- Prepare for AWS SDK and Azure SDK authentication.

---

# ⚠ Security Best Practices

- Never hardcode credentials.
- Never upload secrets to GitHub.
- Use environment variables.
- Rotate API keys regularly.
- Apply the principle of least privilege.

---

# 👨‍💻 Author

**Ravinder Verma**

B.Tech Information Technology

Aspiring Cloud Security Engineer

Learning AWS | Azure | Python | DevSecOps