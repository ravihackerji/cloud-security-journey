# Interview Questions – REST APIs & Python Requests

## Beginner Level

### 1. What is a REST API?

**Answer**

A REST API is a web service that follows REST principles and allows applications to communicate over HTTP.

---

### 2. What is an API?

**Answer**

An API (Application Programming Interface) enables two software applications to communicate by exchanging requests and responses.

---

### 3. Which Python library is commonly used for REST APIs?

**Answer**

The `requests` library.

---

### 4. What does requests.get() do?

**Answer**

It sends an HTTP GET request to retrieve data from a server.

---

### 5. What is an Endpoint?

**Answer**

An endpoint is the URL where an API can be accessed.

Example:

```
https://api.github.com
```

---

## Intermediate Level

### 6. What are HTTP Methods?

**Answer**

HTTP methods define the action to perform on a resource.

- GET → Retrieve
- POST → Create
- PUT → Update
- DELETE → Remove

---

### 7. Difference between GET and POST?

**Answer**

GET retrieves data from a server.

POST sends data to create a new resource.

---

### 8. What is a Status Code?

**Answer**

A status code is a numerical response from the server that indicates whether the request was successful or failed.

---

### 9. What does Status Code 200 mean?

**Answer**

The request was successful.

---

### 10. Explain common HTTP Status Codes.

**Answer**

- 200 → OK
- 201 → Created
- 400 → Bad Request
- 401 → Unauthorized
- 403 → Forbidden
- 404 → Not Found
- 500 → Internal Server Error

---

## Advanced Level

### 11. Why do Cloud Security Engineers use REST APIs?

**Answer**

To automate cloud operations such as inventory collection, IAM management, security monitoring, compliance reporting, and incident response.

---

### 12. How does Python process API responses?

**Answer**

Using `response.json()`, which converts the JSON response into a Python dictionary.

---

### 13. Why should status codes always be checked?

**Answer**

Because APIs may return errors such as authentication failures, permission issues, or server errors. Checking the status code ensures the program handles these situations correctly.

---

### 14. How does Boto3 relate to REST APIs?

**Answer**

Boto3 is the AWS SDK for Python. Internally, it communicates with AWS services using HTTPS and REST-style APIs, then converts the responses into Python objects.

---

### 15. How can this project be improved?

**Answer**

- Add authentication using API keys or Bearer tokens.
- Store secrets in environment variables.
- Save responses to CSV or JSON.
- Add logging.
- Handle exceptions.
- Build a web dashboard.

---

# Scenario-Based Interview Questions

### 16. Your Python script receives HTTP Status Code 401. What does it indicate?

**Answer**

It indicates an authentication failure. The API credentials are missing, invalid, or expired.

---

### 17. Your script receives HTTP Status Code 404. What should you check?

**Answer**

Verify that the API endpoint URL is correct and that the requested resource exists.

---

### 18. Your API request returns HTTP Status Code 500. What does it mean?

**Answer**

The error occurred on the server side. The client request may be valid, but the server encountered an internal problem.

---

### 19. Why is JSON commonly used with REST APIs?

**Answer**

JSON is lightweight, easy to read, language-independent, and can be easily converted into Python dictionaries for processing.

---

### 20. Explain the complete API communication flow.

**Answer**

Python Script

↓

Requests Library

↓

HTTP Request

↓

REST API Endpoint

↓

JSON Response

↓

Python Dictionary

↓

Process Data

---

# Quick Revision

| Topic | Remember |
|--------|----------|
| API | Communication between applications |
| REST API | Web service using HTTP |
| Endpoint | API URL |
| GET | Read data |
| POST | Create data |
| PUT | Update data |
| DELETE | Delete data |
| JSON | Data exchange format |
| Requests | Python library for HTTP |
| response.json() | Converts JSON to Python dictionary |

---

# HR Interview Question

### Q: Why are REST APIs important for Cloud Security Engineers?

**Answer**

REST APIs enable automation of cloud operations. They allow engineers to retrieve cloud resources, monitor security findings, manage IAM, perform compliance checks, and integrate with third-party security tools without manual intervention.