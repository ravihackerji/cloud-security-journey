# Interview Questions – Python Exception Handling

## Beginner Level

### 1. What is an Exception?

**Answer**

An exception is an error that occurs during the execution of a program and interrupts the normal flow of execution.

---

### 2. Why do we use Exception Handling?

**Answer**

Exception handling prevents programs from crashing and allows errors to be handled gracefully.

---

### 3. What is the purpose of try?

**Answer**

The `try` block contains code that might raise an exception.

---

### 4. What is the purpose of except?

**Answer**

The `except` block handles exceptions if they occur in the `try` block.

---

### 5. What is FileNotFoundError?

**Answer**

It occurs when Python tries to open a file that does not exist.

---

## Intermediate Level

### 6. What is the purpose of else?

**Answer**

The `else` block executes only if no exception occurs in the `try` block.

---

### 7. What is the purpose of finally?

**Answer**

The `finally` block always executes, regardless of whether an exception occurs or not.

---

### 8. Why should you avoid using a bare except?

**Answer**

A bare `except:` catches all exceptions, including unexpected ones, making debugging difficult. It is better to catch specific exceptions.

---

### 9. Why combine Logging with Exception Handling?

**Answer**

Logging records errors permanently, making it easier to troubleshoot production issues and maintain audit trails.

---

### 10. What does Exception as error mean?

**Answer**

It stores the exception object in the variable `error`, allowing the program to display or log the actual error message.

---

## Advanced Level

### 11. How is Exception Handling used in Cloud Security?

**Answer**

Cloud security scripts use exception handling to recover from API failures, missing files, permission issues, network problems, and invalid data while continuing to process remaining resources.

---

### 12. Give an AWS example where Exception Handling is useful.

**Answer**

When scanning thousands of S3 buckets using Boto3, one bucket may return an access error. The script should log the error and continue scanning the remaining buckets.

---

### 13. What are the benefits of Exception Handling?

**Answer**

- Prevents crashes
- Improves reliability
- Makes debugging easier
- Supports production automation
- Improves user experience

---

### 14. Why is finally important?

**Answer**

It ensures cleanup operations such as closing files, database connections, or network sessions always occur.

---

### 15. How would you improve this project?

**Answer**

- Read users directly from AWS IAM using Boto3.
- Upload logs to CloudWatch.
- Send email alerts.
- Store reports in Amazon S3.
- Schedule daily execution using AWS Lambda or cron.

---

# Scenario-Based Interview Questions

### 16. Your Python script scans 2,000 EC2 instances. One API request fails because of a timeout. What should the script do?

**Answer**

Catch the exception, log the timeout, continue scanning the remaining instances, and include the failure in the final report.

---

### 17. A CloudTrail log file is missing. How should your automation behave?

**Answer**

Handle the FileNotFoundError, record the issue in the log file, notify the user if appropriate, and exit gracefully instead of crashing.

---

# Quick Revision

| Topic | Remember |
|--------|----------|
| try | Risky code |
| except | Handles errors |
| else | Runs if no error occurs |
| finally | Always runs |
| Exception | Base class for many runtime errors |
| FileNotFoundError | File does not exist |
| Logging | Records errors permanently |

---

# HR Interview Question

**Q:** Why is reliability important in automation?

**Answer:**

Automation often runs without human supervision. Reliable scripts handle errors gracefully, continue processing whenever possible, and produce useful logs for troubleshooting and auditing.