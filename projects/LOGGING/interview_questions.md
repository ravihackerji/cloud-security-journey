# Interview Questions – Python Logging

## Beginner Level

### 1. What is logging in Python?

**Answer**

Logging is the process of recording events that occur while a program executes. It helps with monitoring, debugging, auditing, and troubleshooting.

---

### 2. Why is logging better than print()?

**Answer**

Logging provides timestamps, severity levels, and permanent log files, while print() only displays temporary output on the screen.

---

### 3. Which module is used for logging?

**Answer**

Python's built-in `logging` module.

---

### 4. What does logging.basicConfig() do?

**Answer**

It configures the logging system, including log level, file name, and log format.

---

### 5. What is a log file?

**Answer**

A log file stores information about a program's execution for future analysis.

---

## Intermediate Level

### 6. Name the five logging levels.

**Answer**

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

---

### 7. What is the purpose of INFO logs?

**Answer**

INFO logs record normal execution of the application.

Example:

```
Script Started
```

---

### 8. When should WARNING be used?

**Answer**

When the program detects an unusual situation but can continue running.

Example:

```
User without MFA
```

---

### 9. When should ERROR be used?

**Answer**

When an operation fails but the application may still continue.

Example:

```
AWS API Connection Failed
```

---

### 10. What is CRITICAL?

**Answer**

A severe error that may stop the program.

Example:

```
Unable to connect to AWS
Program Terminated
```

---

## Advanced Level

### 11. Why are timestamps important?

**Answer**

Timestamps help determine exactly when events occurred during execution.

---

### 12. Why are log files important in Cloud Security?

**Answer**

They provide an audit trail for investigations, troubleshooting, monitoring, and compliance.

---

### 13. Where are logs commonly stored in AWS?

**Answer**

Examples include:

- Amazon CloudWatch Logs
- Amazon S3
- Security Information and Event Management (SIEM) platforms

---

### 14. Give examples of Cloud Security tasks that require logging.

**Answer**

- IAM auditing
- CloudTrail analysis
- Security Hub reporting
- GuardDuty monitoring
- Compliance automation
- Incident response

---

### 15. How would you improve this project?

**Answer**

- Integrate with AWS CloudWatch.
- Email log reports.
- Schedule daily execution.
- Store logs in S3.
- Add exception handling.
- Build a dashboard.

---

# Quick Revision

| Topic | Remember |
|--------|----------|
| logging | Records program execution |
| INFO | Normal execution |
| WARNING | Potential issue |
| ERROR | Operation failed |
| CRITICAL | Severe failure |
| Log File | Permanent record |
| logging.basicConfig() | Configure logging |

---

# HR Interview Question

**Q:** Why is logging important in production applications?

**Answer:**

Logging helps engineers monitor applications, troubleshoot failures, investigate incidents, maintain audit trails, and understand how software behaves after deployment. It is an essential practice for building reliable and maintainable production systems.