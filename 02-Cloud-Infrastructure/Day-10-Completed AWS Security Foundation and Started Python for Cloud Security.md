# Day 10 – AWS Security Services & Python for Cloud Security

## 📅 Date

28 June 2026

---

# 🎯 Objective

Today I completed the AWS Security Foundation by learning the core security services used by Cloud Security Engineers and started Python for Cloud Security, focusing on JSON and professional file handling.

---

# ☁️ AWS Security Services Learned

## 1. AWS CloudTrail

### Purpose

Records every important API activity performed in an AWS account.

### Key Learnings

* Records who performed an action.
* Records when the action occurred.
* Records the source IP address.
* Used for auditing and incident response.
* Stores logs in Amazon S3.

### Azure Equivalent

Azure Activity Logs

---

## 2. AWS CloudWatch

### Purpose

Monitors the health and performance of AWS resources.

### Key Learnings

* Collects metrics.
* Generates alarms.
* Stores application logs.
* Used for monitoring CPU, memory (via agent), network, and disk activity.

### Azure Equivalent

Azure Monitor

---

## 3. AWS Config

### Purpose

Continuously checks whether AWS resources comply with organizational security policies.

### Key Learnings

* Records resource configurations.
* Evaluates Config Rules.
* Detects configuration drift.
* Helps maintain compliance.

### Azure Equivalent

Azure Policy

---

## 4. Amazon GuardDuty

### Purpose

Provides intelligent threat detection.

### Key Learnings

* Detects suspicious activity.
* Uses CloudTrail, DNS Logs, and VPC Flow Logs.
* Generates security findings.
* Helps identify compromised accounts and malicious behavior.

### Azure Equivalent

Microsoft Defender for Cloud

---

## 5. Amazon Inspector

### Purpose

Identifies vulnerabilities in AWS resources.

### Key Learnings

* Scans EC2 instances.
* Identifies software vulnerabilities (CVEs).
* Prioritizes findings by severity.
* Supports proactive vulnerability management.

### Azure Equivalent

Microsoft Defender for Cloud Vulnerability Assessment

---

## 6. AWS Security Hub

### Purpose

Provides a centralized dashboard for AWS security findings.

### Key Learnings

* Aggregates findings from multiple AWS security services.
* Helps prioritize security issues.
* Supports security standards and compliance reporting.

---

# 🔐 AWS Security Workflow

```text
IAM
↓

CloudTrail
↓

CloudWatch
↓

AWS Config
↓

GuardDuty
↓

Inspector
↓

Security Hub
```

Each service has a unique role:

* IAM → Access Control
* CloudTrail → Audit
* CloudWatch → Monitoring
* AWS Config → Compliance
* GuardDuty → Threat Detection
* Inspector → Vulnerability Assessment
* Security Hub → Centralized Security Dashboard

---

# 🐍 Python for Cloud Security

## Why Python?

Python is the most widely used language for cloud security automation because it is simple, powerful, and integrates easily with cloud APIs.

Typical automation tasks include:

* IAM auditing
* S3 security scanning
* EC2 inventory
* CloudTrail log analysis
* Compliance reporting
* Security dashboards

---

# JSON Fundamentals

JSON is the standard format used by cloud services to exchange structured data.

### Important Concepts

* Object → {}
* Array → []
* Key → Value
* Strings use double quotes

Python Mapping

| Python     | JSON   |
| ---------- | ------ |
| Dictionary | Object |
| List       | Array  |
| True       | true   |
| False      | false  |
| None       | null   |

JSON is heavily used in:

* CloudTrail
* IAM Policies
* GuardDuty Findings
* Security Hub
* AWS APIs
* Azure APIs

---

# Python JSON Module

Important functions:

* json.dump()
* json.dumps()
* json.load()
* json.loads()

### Memory Trick

* dump() → File
* dumps() → String
* load() → File
* loads() → String

---

# Professional File Handling

Best Practice:

Always use:

```python
with open("file.txt", "r") as file:
    data = file.read()
```

instead of manually opening and closing files.

### File Modes

* r → Read
* w → Write
* a → Append
* x → Create

### Cloud Security Use Cases

* Reading CloudTrail logs
* Parsing SIEM logs
* Writing compliance reports
* Processing security findings
* Log analysis

---

# ⭐ Key Interview Questions

### Q1. Difference between CloudTrail and CloudWatch?

CloudTrail records AWS API activity, while CloudWatch monitors resource health and performance.

---

### Q2. Difference between GuardDuty and Inspector?

GuardDuty detects suspicious or malicious activity.

Inspector identifies vulnerabilities before they are exploited.

---

### Q3. What is AWS Config?

AWS Config continuously evaluates AWS resources against security and compliance rules.

---

### Q4. What is Security Hub?

Security Hub aggregates findings from multiple AWS security services into a centralized dashboard.

---

### Q5. Why is JSON important?

JSON is the standard format used by cloud APIs for exchanging structured data.

---

### Q6. Difference between dump() and dumps()?

dump() writes JSON to a file.

dumps() converts a Python object into a JSON string.

---

### Q7. Why should with open() be used?

It automatically closes files and prevents resource leaks.

---

# 📚 What I Learned Today

* Completed the AWS Security Foundation.
* Understood the responsibilities of major AWS security services.
* Learned how cloud security services complement each other.
* Started Python for Cloud Security.
* Learned JSON fundamentals.
* Learned Python's json module.
* Learned production-style file handling.

---

# 🚀 Next Goal

* CSV Processing
* Python Logging
* Exception Handling
* Requests Library
* REST APIs
* Boto3
* AWS Automation Projects

---

# 💡 Personal Reflection

Today's learning connected cloud security concepts with Python automation. I now understand that cloud security engineers don't just configure services—they automate monitoring, compliance, reporting, and incident response using Python.
