# Interview Notes Update – Day 10

## AWS Security Foundation + Python for Cloud Security

---

# AWS CloudTrail

### Q1. What is AWS CloudTrail?

**Answer:**
AWS CloudTrail is an audit service that records AWS API activity. It helps determine who performed an action, when it occurred, from where it originated, and whether it succeeded.

---

### Q2. What information does CloudTrail record?

**Answer:**

* API calls
* User or Role
* Timestamp
* Source IP Address
* AWS Service
* Event Name
* Success or Failure

---

### Q3. Where are CloudTrail logs stored?

**Answer:**
CloudTrail logs are commonly stored in Amazon S3 for long-term retention and analysis.

---

### Q4. CloudTrail vs CloudWatch?

**Answer:**

| CloudTrail            | CloudWatch                   |
| --------------------- | ---------------------------- |
| Records API activity  | Monitors system health       |
| Used for auditing     | Used for monitoring          |
| Answers "Who did it?" | Answers "How is the system?" |

---

# AWS CloudWatch

### Q5. What is CloudWatch?

**Answer:**
CloudWatch is AWS's monitoring service. It collects metrics, logs, and alarms to monitor the health and performance of AWS resources.

---

### Q6. What is a CloudWatch Metric?

**Answer:**
A metric is a numerical measurement collected over time, such as CPUUtilization, NetworkIn, or DiskReadOps.

---

### Q7. What is a CloudWatch Alarm?

**Answer:**
A CloudWatch Alarm monitors a metric and performs an action, such as sending a notification, when a defined threshold is reached.

---

# AWS Config

### Q8. What is AWS Config?

**Answer:**
AWS Config continuously records AWS resource configurations and evaluates them against compliance rules.

---

### Q9. What is a Config Rule?

**Answer:**
A Config Rule defines the desired configuration of AWS resources and checks whether they comply with organizational policies.

---

### Q10. What is Compliance?

**Answer:**
Compliance means that AWS resources follow the organization's required security and operational rules.

---

# Amazon GuardDuty

### Q11. What is Amazon GuardDuty?

**Answer:**
Amazon GuardDuty is AWS's intelligent threat detection service. It analyzes CloudTrail, VPC Flow Logs, DNS logs, and other supported sources to detect suspicious activity.

---

### Q12. What is a GuardDuty Finding?

**Answer:**
A Finding is a security alert generated when GuardDuty detects potentially malicious or suspicious behavior.

---

### Q13. GuardDuty vs Inspector?

**Answer:**

GuardDuty detects attacks or suspicious behavior.

Inspector identifies vulnerabilities before they are exploited.

---

# Amazon Inspector

### Q14. What is Amazon Inspector?

**Answer:**
Amazon Inspector scans supported AWS resources for known vulnerabilities and security weaknesses.

---

### Q15. What is a CVE?

**Answer:**
CVE (Common Vulnerabilities and Exposures) is a standardized identifier assigned to publicly known software vulnerabilities.

---

### Q16. What should you do after receiving a Critical vulnerability finding?

**Answer:**
Prioritize remediation by validating the finding, assessing the impact, applying patches or updates, and verifying that the vulnerability has been resolved.

---

# AWS Security Hub

### Q17. What is AWS Security Hub?

**Answer:**
AWS Security Hub is a centralized security dashboard that aggregates and prioritizes findings from multiple AWS security services.

---

### Q18. Which AWS services integrate with Security Hub?

**Answer:**
Examples include:

* GuardDuty
* Inspector
* AWS Config
* IAM Access Analyzer
* Firewall Manager

---

### Q19. Why is Security Hub useful?

**Answer:**
It provides a single location to view, prioritize, and manage security findings across AWS environments.

---

# Python for Cloud Security

### Q20. Why is Python the preferred language for Cloud Security?

**Answer:**
Python is simple to learn, has excellent automation capabilities, official cloud SDKs (Boto3 and Azure SDK), and strong support for APIs, JSON, and automation workflows.

---

### Q21. What is an API?

**Answer:**
An API (Application Programming Interface) allows applications to communicate with each other. Python uses AWS APIs to interact with AWS services.

---

### Q22. What is Boto3?

**Answer:**
Boto3 is the official AWS SDK for Python that enables Python programs to manage AWS resources.

---

# JSON

### Q23. What is JSON?

**Answer:**
JSON (JavaScript Object Notation) is a lightweight data-interchange format used by cloud services to exchange structured information.

---

### Q24. Why is JSON important in Cloud Computing?

**Answer:**
Cloud services exchange requests and responses in JSON format, making it essential for interacting with cloud APIs.

---

### Q25. Difference between dump() and dumps()?

**Answer:**

* dump() writes JSON to a file.
* dumps() converts a Python object into a JSON string.

---

### Q26. Difference between load() and loads()?

**Answer:**

* load() reads JSON from a file.
* loads() converts a JSON string into a Python object.

---

# Professional File Handling

### Q27. Why is with open() preferred?

**Answer:**
It automatically closes the file after use, preventing resource leaks and making the code safer and cleaner.

---

### Q28. Difference between "r", "w", and "a" file modes?

**Answer:**

* r → Read existing file.
* w → Write and overwrite existing content.
* a → Append new content to the end of the file.

---

### Q29. Why should large CloudTrail logs be processed line by line?

**Answer:**
Reading line by line reduces memory usage and is more efficient when processing very large log files.

---

# Scenario-Based Interview Question

### Q30. An EC2 instance suddenly shows 98% CPU utilization. How would you investigate?

**Answer:**

1. Check CloudWatch to confirm the CPUUtilization metric and review recent trends.
2. Review CloudTrail to determine whether any recent API calls modified the instance or related infrastructure.
3. Check GuardDuty for any suspicious activity involving the instance.
4. Review application and system logs to identify the root cause.
5. Determine whether the issue is due to legitimate workload, misconfiguration, or malicious activity.

---

# Quick Revision

* IAM → Controls access.
* CloudTrail → Records API activity.
* CloudWatch → Monitors health.
* AWS Config → Checks compliance.
* GuardDuty → Detects threats.
* Inspector → Finds vulnerabilities.
* Security Hub → Centralized security dashboard.
* JSON → Standard cloud data format.
* Boto3 → Python SDK for AWS.
* with open() → Professional file handling.
