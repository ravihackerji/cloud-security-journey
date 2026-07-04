# Interview Questions – Environment Variables

## Beginner Level

### 1. What is an Environment Variable?

**Answer**

An environment variable is a key-value pair stored by the operating system that applications can access during execution.

---

### 2. Why are Environment Variables used?

**Answer**

They securely store configuration values and sensitive information outside the application source code.

---

### 3. Which Python module is used to access Environment Variables?

**Answer**

The built-in `os` module.

---

### 4. Which function reads an Environment Variable?

**Answer**

```python
os.getenv()
```

---

### 5. What happens if the Environment Variable does not exist?

**Answer**

`os.getenv()` returns `None`, or the default value if one is provided.

Example:

```python
os.getenv("API_KEY", "Not Configured")
```

---

## Intermediate Level

### 6. Why should API Keys never be hardcoded?

**Answer**

Hardcoded credentials can be exposed through source code repositories, making systems vulnerable to unauthorized access.

---

### 7. Give examples of secrets stored as Environment Variables.

**Answer**

- AWS Access Key
- AWS Secret Access Key
- Azure Client Secret
- Database Password
- GitHub Token
- Slack Webhook
- API Keys

---

### 8. What is the advantage of Environment Variables?

**Answer**

They separate sensitive configuration from application code, making applications more secure and easier to deploy across different environments.

---

### 9. What is os.getenv()?

**Answer**

It retrieves the value of an environment variable.

Example:

```python
import os

api_key = os.getenv("API_KEY")
```

---

### 10. Why should secrets never be printed?

**Answer**

Printing secrets may expose credentials in terminal output, logs, or monitoring systems.

---

## Advanced Level

### 11. How does AWS Boto3 use Environment Variables?

**Answer**

Boto3 automatically checks for AWS credentials stored in environment variables such as:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION

---

### 12. How are Environment Variables used in Azure?

**Answer**

Azure SDKs commonly use environment variables for:

- AZURE_CLIENT_ID
- AZURE_CLIENT_SECRET
- AZURE_TENANT_ID
- AZURE_SUBSCRIPTION_ID

---

### 13. Why are Environment Variables important in DevSecOps?

**Answer**

They keep secrets out of source code and allow secure configuration across development, testing, and production environments.

---

### 14. What is the Principle of Least Privilege?

**Answer**

Grant only the minimum permissions required to complete a task.

---

### 15. Why should credentials be rotated?

**Answer**

Regular rotation reduces the impact of compromised or leaked credentials.

---

# Cloud Security Interview Questions

### 16. Why are Environment Variables important in Cloud Security?

**Answer**

They protect sensitive credentials and reduce the risk of accidental exposure in code repositories.

---

### 17. Give examples where Environment Variables are used.

**Answer**

- AWS Lambda
- Docker
- Kubernetes
- GitHub Actions
- Jenkins
- Terraform
- Azure Functions

---

### 18. What is the difference between Environment Variables and hardcoded credentials?

**Answer**

Environment variables store secrets outside the code, while hardcoded credentials are embedded in the source code and are much easier to expose.

---

### 19. What would you do if AWS credentials were accidentally pushed to GitHub?

**Answer**

- Revoke or rotate the credentials immediately.
- Remove them from the repository history.
- Review IAM activity.
- Create new credentials.
- Follow secure storage practices going forward.

---

### 20. Why should IAM Roles be preferred over Access Keys on AWS?

**Answer**

IAM Roles provide temporary credentials managed by AWS, reducing the need to store long-term access keys and improving overall security.

---

# Scenario-Based Questions

### 21. Your Python script cannot find the API_KEY environment variable. What should you do?

**Answer**

Check that the variable is set correctly, verify its name, restart the terminal if needed, and provide a sensible default or error message.

---

### 22. Your application prints AWS Secret Keys to the console. Why is this a problem?

**Answer**

It exposes sensitive credentials that could be captured in logs or screenshots, increasing the risk of unauthorized access.

---

### 23. Why should Environment Variables be used in CI/CD pipelines?

**Answer**

They allow pipelines to access secrets securely without embedding them in configuration files or source code.

---

### 24. Explain the Environment Variable workflow.

**Answer**

```
Operating System

↓

Environment Variable

↓

Python os.getenv()

↓

Application

↓

Authentication
```

---

### 25. How will this topic help with AWS Boto3?

**Answer**

Boto3 automatically reads AWS credentials from environment variables, allowing Python scripts to authenticate securely without hardcoding secrets.

---

# HR Interview Question

### Why is secure credential management important?

**Answer**

Proper credential management protects cloud resources, prevents unauthorized access, supports compliance, and follows industry security best practices.

---

# Quick Revision

| Topic | Remember |
|--------|----------|
| Environment Variable | Stores configuration outside the code |
| os Module | Accesses operating system features |
| os.getenv() | Reads environment variables |
| Hardcoding | Security risk |
| AWS_ACCESS_KEY_ID | AWS Access Key |
| AWS_SECRET_ACCESS_KEY | AWS Secret Key |
| Least Privilege | Minimum required permissions |
| IAM Roles | Preferred over long-term access keys |
| Secret Rotation | Regularly update credentials |
| Never Upload Secrets | Keep credentials out of GitHub |