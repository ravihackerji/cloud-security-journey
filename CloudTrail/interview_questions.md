# AWS CloudTrail Interview Questions

## Beginner Level

### 1. What is AWS CloudTrail?

Answer:

AWS CloudTrail is an auditing service that records AWS API activity across an AWS account.

---

### 2. What information does CloudTrail record?

Answer:

- User
- Event Name
- Event Time
- AWS Service
- Source IP
- Region
- Request Details
- Result

---

### 3. Why is CloudTrail important?

Answer:

It helps monitor account activity, investigate incidents, and maintain compliance.

---

### 4. Is CloudTrail enabled by default?

Answer:

Event History for management events is available by default, while creating trails provides ongoing logging and delivery to services like Amazon S3.

---

### 5. What are Management Events?

Answer:

Management Events record changes made to AWS resources.

Examples:

- CreateUser
- StartInstances
- DeleteBucket

---

## Intermediate Level

### 6. What are Data Events?

Answer:

Data Events record operations performed on data stored in services like Amazon S3 and AWS Lambda.

---

### 7. Difference between Management Events and Data Events?

Answer:

Management Events monitor resource management operations.

Data Events monitor access to objects and application data.

---

### 8. CloudTrail vs CloudWatch?

Answer:

CloudTrail records AWS API activity.

CloudWatch monitors logs, metrics, alarms, and operational health.

---

### 9. How does CloudTrail help Incident Response?

Answer:

It identifies:

- Who performed an action
- When it happened
- Source IP
- AWS Region
- Whether it succeeded

---

### 10. Where are CloudTrail logs stored?

Answer:

CloudTrail Event History is available in the console, and trails can deliver logs to Amazon S3. They can also be integrated with CloudWatch Logs for monitoring.

---

## Advanced Level

### 11. An EC2 instance was terminated unexpectedly. Which AWS service helps identify who deleted it?

Answer:

AWS CloudTrail.

---

### 12. Which CloudTrail event should you search for?

Answer:

TerminateInstances

---

### 13. How would you investigate an unauthorized IAM User creation?

Answer:

Search for the CreateUser event and review:

- IAM User
- Source IP
- Timestamp
- Region
- Request Details

---

### 14. Why is CloudTrail important for compliance?

Answer:

It provides an immutable audit trail that supports standards such as ISO 27001, PCI DSS, and SOC 2 by helping demonstrate accountability and traceability.

---

### 15. How can CloudTrail be automated with Python?

Answer:

Using Boto3 to:

- Retrieve events
- Search logs
- Generate audit reports
- Detect suspicious activities
- Export findings to CSV or dashboards