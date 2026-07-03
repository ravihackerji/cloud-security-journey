# Interview Questions – Python Requests & REST APIs

## Beginner Level

### 1. What is an API?

**Answer:**

An API (Application Programming Interface) is a set of rules that allows two software applications to communicate with each other.

Example:

A Python script communicates with AWS using an API.

---

### 2. What is a REST API?

**Answer:**

A REST API is a web service that follows REST principles and uses HTTP methods such as GET, POST, PUT, and DELETE to exchange data.

---

### 3. What is the Requests library?

**Answer:**

Requests is a third-party Python library used to send HTTP requests and receive responses from web servers or APIs.

Installation:

```bash
pip install requests
```

---

### 4. Why is Requests popular?

**Answer:**

Because it provides a simple, readable, and efficient way to communicate with web APIs compared to Python's built-in HTTP libraries.

---

### 5. What is an Endpoint?

**Answer:**

An endpoint is the URL through which an API can be accessed.

Example:

```
https://api.github.com
```

---

## Intermediate Level

### 6. Explain HTTP Methods.

**Answer**

| Method | Purpose |
|---------|---------|
| GET | Retrieve data |
| POST | Create new resource |
| PUT | Update existing resource |
| DELETE | Delete resource |

---

### 7. Difference between GET and POST?

**Answer**

GET retrieves information.

POST sends information to create a new resource.

---

### 8. What is an HTTP Status Code?

**Answer**

A status code is a response sent by the server indicating whether the request was successful or failed.

---

### 9. Explain these Status Codes.

**200**

Request Successful.

---

**201**

Resource Created Successfully.

---

**400**

Bad Request.

The client sent an invalid request.

---

**401**

Unauthorized.

Authentication is required.

---

**403**

Forbidden.

The client is authenticated but does not have permission.

---

**404**

Resource Not Found.

---

**500**

Internal Server Error.

---

### 10. What does response.status_code return?

**Answer**

It returns the HTTP status code received from the server.

Example:

```python
print(response.status_code)
```

---

### 11. What does response.json() do?

**Answer**

It converts a JSON response into a Python dictionary.

---

### 12. Why is JSON commonly used?

**Answer**

Because it is lightweight, easy to read, language-independent, and easily converted into Python objects.

---

## Advanced Level

### 13. Explain the complete REST API workflow.

**Answer**

```
Python Script

↓

Requests Library

↓

HTTP Request

↓

REST API Endpoint

↓

Cloud Service

↓

JSON Response

↓

Python Dictionary

↓

Automation
```

---

### 14. How does AWS use REST APIs?

**Answer**

AWS services expose APIs over HTTPS.

The AWS SDK (Boto3) internally sends API requests and converts responses into Python objects.

---

### 15. How does Azure use REST APIs?

**Answer**

Azure SDK communicates with Azure Resource Manager APIs over HTTPS and returns JSON responses.

---

### 16. What is the difference between HTTP and REST?

**Answer**

HTTP is a communication protocol.

REST is an architectural style that uses HTTP.

---

### 17. What is an API Header?

**Answer**

Headers contain additional information about the request.

Examples:

- Authorization
- Content-Type
- Accept

---

### 18. What is Content-Type?

**Answer**

It tells the server the format of the request body.

Example:

```
Content-Type: application/json
```

---

### 19. Why should status codes always be checked?

**Answer**

Because APIs may fail due to authentication errors, permission issues, invalid requests, or server failures.

Checking the status code prevents incorrect assumptions and improves error handling.

---

### 20. Why should Requests be combined with Exception Handling?

**Answer**

Network failures, timeouts, and DNS issues can occur.

Exception handling prevents the application from crashing and allows errors to be logged.

Example:

```python
try:
    response = requests.get(url)
except requests.exceptions.RequestException as error:
    print(error)
```

---

# Cloud Security Interview Questions

### 21. Why do Cloud Security Engineers need REST APIs?

**Answer**

Cloud Security Engineers use REST APIs to automate cloud security operations such as:

- IAM Auditing
- Security Monitoring
- Compliance Checks
- Incident Response
- Threat Detection
- Resource Inventory

---

### 22. Give real examples of APIs used in Cloud Security.

**Answer**

- AWS API
- Azure Resource Manager API
- Microsoft Graph API
- GitHub API
- VirusTotal API
- CrowdStrike API
- Splunk API
- Sentinel API
- ServiceNow API

---

### 23. How would you collect GuardDuty findings using Python?

**Answer**

A Python script sends API requests (or uses Boto3), retrieves GuardDuty findings in JSON format, processes the data, generates a report, and logs the results.

---

### 24. How would you automate IAM auditing?

**Answer**

Use Python with the AWS SDK (Boto3) to retrieve IAM users, check MFA status and permissions, identify risks, and generate compliance reports.

---

### 25. Why is API automation better than manual work?

**Answer**

API automation is faster, consistent, scalable, reduces human error, supports scheduled execution, and can integrate with monitoring and alerting systems.

---

# Scenario-Based Questions

### 26. Your API returns 401 Unauthorized. What does it mean?

**Answer**

Authentication failed. The API key, token, or credentials are missing, invalid, or expired.

---

### 27. Your API returns 403 Forbidden. What would you check?

**Answer**

Verify that the authenticated user or role has the required permissions to access the requested resource.

---

### 28. Your API returns 404 Not Found.

What would you do?

**Answer**

- Verify the endpoint URL.
- Confirm the resource exists.
- Check API version.
- Review request parameters.

---

### 29. Your API returns 500 Internal Server Error.

How would you respond?

**Answer**

The issue is on the server side. Retry the request if appropriate, review logs, and contact the service provider if the problem persists.

---

### 30. Your automation suddenly stops working after months.

How would you troubleshoot?

**Answer**

1. Check logs.
2. Verify API endpoint.
3. Validate authentication.
4. Check status code.
5. Test network connectivity.
6. Review recent API changes.
7. Verify rate limits.
8. Re-run with debugging enabled.

---

# HR Interview Question

### Why are APIs important in Cloud Security?

**Answer**

APIs enable secure and automated communication with cloud services. They allow engineers to retrieve resources, enforce security policies, monitor environments, automate compliance checks, and integrate with security platforms efficiently.

---

# Quick Revision

| Topic | Remember |
|--------|----------|
| API | Communication between applications |
| REST API | API using HTTP principles |
| Endpoint | API URL |
| GET | Read |
| POST | Create |
| PUT | Update |
| DELETE | Delete |
| JSON | Data exchange format |
| Requests | Python library for HTTP communication |
| response.json() | Converts JSON to Python dictionary |
| Status Code | Indicates request result |
| Headers | Metadata sent with requests |