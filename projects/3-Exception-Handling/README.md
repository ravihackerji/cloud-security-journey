# Secure File Reader using Python Exception Handling

## 📌 Project Overview

This project demonstrates how Cloud Security Engineers build reliable Python automation scripts using **Exception Handling** and **Logging**.

The script safely reads a CSV file containing IAM user information. If the file is missing or an unexpected error occurs, the script handles the error gracefully, records it in a log file, and continues execution without crashing.

This reflects how production cloud security automation should behave.

---

# 🎯 Objective

- Learn Python Exception Handling.
- Prevent application crashes.
- Handle missing files safely.
- Record errors using the logging module.
- Understand production-grade error handling.

---

# 🛠 Technologies Used

- Python 3
- csv Module
- logging Module

---

# 📂 Project Structure

```
Day-07-Exception-Handling/
│
├── secure_file_reader.py
├── users.csv
├── error.log
├── README.md
└── interview_questions.md
```

---

# 🚀 Project Workflow

```
Start Program
      │
      ▼
Open users.csv
      │
      ▼
Read User Data
      │
      ▼
Any Error?
   │         │
 No         Yes
 │           │
 ▼           ▼
Display     Log Error
Users        │
 │           ▼
 └──────► Finish Program
```

---

# 📜 Features

- Uses `try`
- Uses `except`
- Uses `finally`
- Handles missing files
- Handles unexpected exceptions
- Writes logs to `error.log`
- Demonstrates production-level coding practices

---

# 📄 Sample Input (users.csv)

```
User,MFA
Admin,Enabled
John,Disabled
Alice,Enabled
Bob,Disabled
```

---

# ▶ Expected Output

```
Users in File:

Admin - Enabled
John - Disabled
Alice - Enabled
Bob - Disabled

Program Finished.
```

---

# ❌ If File is Missing

```
Error: users.csv not found.

Program Finished.
```

---

# 📄 Sample error.log

```
2026-06-29 11:20:12 | ERROR | users.csv file not found.
2026-06-29 11:20:12 | INFO | Program Finished.
```

---

# ☁ Cloud Security Use Case

Exception handling is used in:

- AWS IAM Automation
- CloudTrail Analysis
- GuardDuty Processing
- Security Hub Reporting
- Azure Resource Auditing
- Compliance Automation
- Incident Response Scripts

If one AWS API request fails, the automation should log the error and continue processing other resources instead of stopping completely.

---

# 🌍 Real-World Applications

- IAM Auditing
- S3 Inventory Collection
- Cloud Compliance Checks
- Log Processing
- Vulnerability Reporting
- Automated Incident Response

---

# 🚀 Future Improvements

- Read IAM users directly using Boto3.
- Email error reports automatically.
- Store logs in Amazon CloudWatch.
- Upload reports to Amazon S3.
- Send Slack or Microsoft Teams notifications.
- Execute automatically using AWS Lambda.

---

# 📚 Key Concepts Learned

- try
- except
- else
- finally
- Exception
- FileNotFoundError
- Logging
- Production Error Handling

---

# 🎯 Learning Outcome

After completing this project, I can:

- Prevent Python scripts from crashing.
- Handle runtime errors professionally.
- Create production-ready automation.
- Log failures for troubleshooting.
- Build reliable cloud security scripts.

---

# 👨‍💻 Author

**Ravinder Verma**

B.Tech Information Technology

Aspiring Cloud Security Engineer

Learning AWS | Azure | Python | DevSecOps
