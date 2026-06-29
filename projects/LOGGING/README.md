# Cloud Security Audit Logger using Python

## 📌 Project Overview

This project demonstrates how professional Cloud Security Engineers use Python's **logging module** to create audit logs for security automation scripts.

Instead of relying on `print()` statements, the script records important events in a log file with timestamps and severity levels.

---

# 🎯 Objective

- Learn Python's built-in `logging` module.
- Generate audit logs automatically.
- Understand production-level logging practices.
- Simulate a Cloud Security audit workflow.

---

# 🛠 Technologies Used

- Python 3
- Logging Module

---

# 📂 Project Structure

```
Day-06-Logging/
│
├── security_logger.py
├── audit.log
├── README.md
└── interview_questions.md
```

---

# 🚀 Project Workflow

```
Start Script
      │
      ▼
Initialize Logging
      │
      ▼
Scan IAM Users
      │
      ▼
Check S3 Buckets
      │
      ▼
Generate Log Entries
      │
      ▼
Save audit.log
      │
      ▼
Script Completed
```

---

# 📜 Code Features

- Uses Python's built-in `logging` module.
- Saves logs to `audit.log`.
- Includes timestamps.
- Uses multiple log levels.
- Demonstrates production-style logging.

---

# 📖 Logging Levels

| Level | Purpose |
|--------|---------|
| DEBUG | Detailed debugging information |
| INFO | General program execution |
| WARNING | Potential security issue |
| ERROR | Failed operation |
| CRITICAL | Critical failure requiring immediate attention |

---

# ▶ Expected Console Output

```
Audit completed successfully.
Check audit.log
```

---

# 📄 Sample audit.log

```
2026-06-29 10:00:01 | INFO | Cloud Security Audit Started
2026-06-29 10:00:02 | INFO | Scanning IAM Users
2026-06-29 10:00:03 | WARNING | User John has MFA Disabled
2026-06-29 10:00:04 | INFO | Scanning S3 Buckets
2026-06-29 10:00:05 | WARNING | Public Bucket Found: company-backup
2026-06-29 10:00:06 | INFO | Generating Security Report
2026-06-29 10:00:07 | INFO | Cloud Security Audit Completed
```

---

# ☁ Cloud Security Use Case

Cloud Security Engineers use logging to:

- Record automation execution.
- Track IAM audits.
- Log security findings.
- Investigate failures.
- Maintain audit trails.
- Troubleshoot production scripts.

---

# 🌍 Real-World Applications

- AWS IAM Auditing
- CloudTrail Analysis
- GuardDuty Monitoring
- Security Hub Reporting
- Incident Response Automation
- SIEM Log Collection

---

# 🚀 Future Improvements

- Send logs to CloudWatch.
- Store logs in Amazon S3.
- Upload logs to Azure Monitor.
- Generate daily audit reports.
- Email log summaries.
- Integrate with AWS Lambda.
- Store logs in Elasticsearch.

---

# 📚 Key Concepts Learned

- logging module
- logging.basicConfig()
- INFO
- WARNING
- ERROR
- CRITICAL
- Log Formatting
- Log Files
- Production Logging

---

# 🎯 Learning Outcome

After completing this project, I can:

- Create professional log files.
- Record execution history.
- Use multiple logging levels.
- Generate audit trails.
- Prepare Python automation scripts for production environments.

---

# 👨‍💻 Author

**Ravinder Verma**

B.Tech IT Student

Aspiring Cloud Security Engineer

Learning AWS | Azure | Python | DevSecOps