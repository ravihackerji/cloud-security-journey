# Secure Credential Reader using Python Environment Variables

## 📌 Project Overview

This project demonstrates how Cloud Security Engineers securely manage sensitive credentials using **Environment Variables** instead of hardcoding secrets inside source code.

The application reads API credentials from the operating system using Python's `os` module and displays only safe information without exposing sensitive values.

This is a fundamental security practice used in AWS, Azure, DevSecOps, CI/CD pipelines, and cloud automation.

---

# 🎯 Objective

- Learn Environment Variables
- Read credentials securely
- Avoid hardcoding secrets
- Protect API Keys
- Prepare for AWS Boto3 Authentication

---

# 🛠 Technologies Used

- Python 3
- os Module
- Environment Variables

---

# 📂 Project Structure

```
Day-11-Environment-Variables/
│
├── secure_credentials.py
├── README.md
├── interview_questions.md
└── sample_output.txt
```

---

# 🚀 Project Workflow

```
Operating System

↓

Environment Variables

↓

Python os Module

↓

os.getenv()

↓

Secure Credential Retrieval

↓

Application
```

---

# 🔐 Why Environment Variables?

Instead of writing:

```python
API_KEY = "abcd123456"
```

Professional developers write:

```python
import os

API_KEY = os.getenv("API_KEY")
```

This prevents credentials from being exposed in source code.

---

# 📜 Features

- Reads API Key
- Reads AWS Access Key
- Reads AWS Secret Access Key
- Uses Default Values
- Hides Sensitive Credentials
- Demonstrates Secure Credential Management

---

# ▶ Expected Output (Variables Not Configured)

```
==================================================
Secure Credential Reader
==================================================

API Key           : Not Configured
AWS Access Key    : Not Configured
AWS Secret Key    : Not Configured
```

---

# ▶ Expected Output (Variables Configured)

```
==================================================
Secure Credential Reader
==================================================

API Key           : CloudSecurity123
AWS Access Key    : AKIA************
AWS Secret Key    : ************
```

---

# ☁ Cloud Security Use Cases

Environment Variables are commonly used to securely store:

- AWS Access Keys
- AWS Secret Keys
- Azure Client Secrets
- Azure Tenant IDs
- GitHub Tokens
- Slack Webhooks
- Database Passwords
- API Keys
- JWT Secrets

---

# 🌍 Real-World Applications

- AWS SDK (Boto3)
- Azure SDK
- Kubernetes Secrets
- Docker Containers
- GitHub Actions
- Jenkins Pipelines
- Terraform
- CI/CD Pipelines
- Security Automation

---

# 🚀 Future Improvements

- Load variables using a `.env` file.
- Use the `python-dotenv` library.
- Connect to AWS using Boto3.
- Validate missing credentials.
- Log authentication events.
- Build a secure configuration manager.

---

# 📚 Key Concepts Learned

- Environment Variables
- os Module
- os.getenv()
- Secure Credential Storage
- Secret Management
- Configuration Management

---

# 🎯 Learning Outcome

After completing this project, I can:

- Store secrets securely.
- Read environment variables in Python.
- Protect API credentials.
- Prepare applications for production.
- Follow cloud security best practices.

---

# ⚠ Security Best Practices

- Never hardcode secrets.
- Never upload API keys to GitHub.
- Never expose credentials in screenshots.
- Use IAM Roles whenever possible.
- Rotate credentials regularly.
- Apply the Principle of Least Privilege.

---

# 👨‍💻 Author

**Ravinder Verma**

B.Tech Information Technology

Aspiring Cloud Security Engineer

Learning AWS | Azure | Python | DevSecOps