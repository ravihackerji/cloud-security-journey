# Interview Questions – Authentication & Authorization

## Beginner Level

### 1. What is Authentication?

**Answer**

Authentication is the process of verifying the identity of a user or application.

---

### 2. What is Authorization?

**Answer**

Authorization determines what an authenticated user or application is allowed to access.

---

### 3. What is the difference between Authentication and Authorization?

**Answer**

Authentication verifies identity.

Authorization verifies permissions.

---

### 4. What is an API Key?

**Answer**

An API Key is a unique identifier used by applications to authenticate API requests.

---

### 5. What is a Bearer Token?

**Answer**

A Bearer Token is an access token included in the Authorization header to authenticate API requests.

---

### 6. What is OAuth?

**Answer**

OAuth is an authorization framework that allows applications to access resources on behalf of a user without exposing the user's password.

---

### 7. What is an Access Token?

**Answer**

An Access Token is a temporary credential used to access protected APIs.

---

### 8. What is an HTTP Header?

**Answer**

Headers contain metadata about an HTTP request or response, such as authentication information and content type.

---

### 9. Why are headers important?

**Answer**

Headers carry authentication credentials, define data formats, and provide additional request information.

---

### 10. Where is a Bearer Token sent?

**Answer**

Inside the Authorization header.

Example:

Authorization: Bearer <token>

---

## Intermediate Level

### 11. Why should credentials never be hardcoded?

**Answer**

Hardcoded credentials can be exposed through source code repositories, making systems vulnerable to unauthorized access.

---

### 12. What is the Principle of Least Privilege?

**Answer**

Users and applications should receive only the minimum permissions required to perform their tasks.

---

### 13. What is IAM?

**Answer**

Identity and Access Management (IAM) controls authentication and authorization for cloud resources.

---

### 14. What happens if authentication fails?

**Answer**

The server usually returns HTTP Status Code 401 Unauthorized.

---

### 15. What happens if authorization fails?

**Answer**

The server usually returns HTTP Status Code 403 Forbidden.

---

### 16. Explain API authentication workflow.

**Answer**

Client

↓

Authentication Credentials

↓

Server Verification

↓

Authorization Check

↓

Response

---

### 17. Why are Access Tokens preferred over passwords?

**Answer**

They are temporary, can have limited permissions, and reduce the need to expose user passwords.

---

### 18. What is Multi-Factor Authentication (MFA)?

**Answer**

MFA requires two or more verification factors to authenticate a user, improving account security.

---

### 19. How can API credentials be stored securely?

**Answer**

Using environment variables, secret management services, or secure vaults.

---

### 20. Why should API Keys be rotated?

**Answer**

Regular rotation reduces the impact of leaked or compromised credentials.

---

## Advanced Level

### 21. How does AWS authenticate API requests?

**Answer**

AWS uses IAM credentials such as Access Key ID and Secret Access Key. Requests are cryptographically signed before reaching AWS services.

---

### 22. What authentication methods are commonly used in Azure?

**Answer**

Microsoft Entra ID, OAuth 2.0, Service Principals, and Managed Identities.

---

### 23. Why do Cloud Security Engineers need authentication knowledge?

**Answer**

Authentication is required to securely access cloud resources, automate security tasks, and integrate with cloud services.

---

### 24. Give examples of APIs requiring authentication.

**Answer**

- AWS APIs
- Azure Resource Manager APIs
- Microsoft Graph API
- GitHub API
- VirusTotal API
- CrowdStrike API
- Splunk API

---

### 25. Explain the difference between an API Key and OAuth.

**Answer**

API Keys identify an application.

OAuth issues temporary tokens for delegated user access and supports more secure authentication flows.

---

# Scenario-Based Questions

### 26. Your API returns HTTP 401 Unauthorized. What do you check?

**Answer**

- API Key
- Access Token
- Token Expiration
- Authentication Configuration

---

### 27. Your API returns HTTP 403 Forbidden. What does it mean?

**Answer**

Authentication succeeded, but the authenticated identity lacks the required permissions.

---

### 28. A developer accidentally pushed AWS credentials to GitHub. What should be done?

**Answer**

- Revoke or rotate the credentials immediately.
- Remove them from the repository history.
- Audit account activity.
- Create new credentials.
- Review IAM permissions.

---

### 29. Why should secrets be stored in environment variables?

**Answer**

They separate sensitive data from source code, reducing the risk of accidental exposure.

---

### 30. How will this topic help in AWS Boto3?

**Answer**

Boto3 requires secure authentication using AWS credentials or IAM roles. Understanding authentication is essential for securely automating AWS services.

---

# HR Interview Question

### Why is Authentication important in Cloud Security?

**Answer**

Authentication ensures that only verified users or applications can access cloud resources, helping protect sensitive data, maintain compliance, and reduce the risk of unauthorized access.

---

# Quick Revision

| Topic | Remember |
|--------|----------|
| Authentication | Verify identity |
| Authorization | Verify permissions |
| API Key | Static credential |
| Bearer Token | Access token |
| OAuth | Delegated authorization |
| IAM | Identity and Access Management |
| 401 | Authentication failed |
| 403 | Permission denied |
| Environment Variables | Secure secret storage |
| Least Privilege | Minimum required permissions |