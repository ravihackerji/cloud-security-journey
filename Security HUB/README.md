# Day 18 - AWS Security Hub

## 📖 Overview

AWS Security Hub is a Cloud Security Posture Management (CSPM) service that centralizes security findings from AWS services and third-party security tools into a single dashboard.

It helps security teams monitor, prioritize, investigate, and remediate security issues across AWS environments.

Security Hub acts as the central command center for AWS security.

---

## 🎯 Learning Objectives

- Understand AWS Security Hub
- Learn Security Findings
- Learn Security Standards
- Understand Security Score
- Learn Integrations
- Understand Automated Response
- Learn Cloud Security Monitoring
- Learn Python (Boto3) Integration

---

## 📚 Topics Covered

- AWS Security Hub
- Security Findings
- AWS Foundational Security Best Practices
- CIS AWS Foundations Benchmark
- Security Score
- EventBridge Integration
- Lambda Automation
- Compliance Monitoring
- Cloud Security Dashboard

---

## 🏗 Architecture

GuardDuty

↓

AWS Config

↓

Inspector

↓

IAM Access Analyzer

↓

Amazon Macie

↓

Third-party Security Tools

↓

AWS Security Hub

↓

Security Dashboard

↓

Security Team

---

## 🔒 Cloud Security Applications

- Centralized Security Monitoring
- Compliance Monitoring
- Incident Investigation
- Risk Prioritization
- Security Dashboard
- Threat Visibility

---

## 💼 Real-world Example

A company has multiple AWS accounts.

GuardDuty reports compromised credentials.

AWS Config reports public S3 buckets.

Inspector reports vulnerable EC2 instances.

Security Hub combines all these findings into one dashboard, allowing the security team to prioritize and respond efficiently.

---

## 🐍 Python Integration

Later in this journey, Security Hub will be automated using:

- Python
- Boto3
- Security Reports
- Compliance Reports
- CSV Export
- Dashboard Automation

---

## 📁 Files

- security_hub_notes.md
- interview_questions.md
- README.md

---

## 🚀 Next Topic

Amazon Inspector