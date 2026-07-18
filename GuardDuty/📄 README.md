# Day 17 - Amazon GuardDuty

## 📖 Overview

Amazon GuardDuty is AWS's intelligent threat detection service that continuously monitors AWS accounts and workloads for malicious or unauthorized activity.

It uses Machine Learning (ML), anomaly detection, and AWS threat intelligence to identify suspicious behavior without requiring customers to manage their own detection infrastructure.

GuardDuty is one of the core AWS security services and plays an essential role in Security Operations Centers (SOC), Incident Response, and Cloud Security.

---

## 🎯 Learning Objectives

- Understand Amazon GuardDuty
- Learn how GuardDuty works
- Understand GuardDuty data sources
- Learn about Findings and Severity Levels
- Explore real-world attack detection
- Understand integrations with AWS security services
- Learn Python (Boto3) integration

---

## 📚 Topics Covered

- Amazon GuardDuty
- Threat Detection
- Machine Learning
- Threat Intelligence
- CloudTrail Analysis
- VPC Flow Logs
- DNS Logs
- Findings
- Severity Levels
- Security Monitoring
- Cloud Security Use Cases

---

## 🏗 Architecture

CloudTrail
VPC Flow Logs
DNS Logs
S3 Protection
EKS Audit Logs

↓

Amazon GuardDuty

↓

Threat Analysis

↓

Security Findings

↓

Security Hub / EventBridge / SNS

↓

Security Team

---

## 🔒 Cloud Security Applications

- Detect Compromised IAM Users
- Detect Stolen AWS Credentials
- Detect Malware Communication
- Detect Cryptocurrency Mining
- Detect Port Scanning
- Detect Data Exfiltration
- Threat Hunting

---

## 💼 Real-world Example

An attacker steals AWS Access Keys and logs in from another country.

GuardDuty detects:

- Unusual login location
- Suspicious API activity
- Privilege escalation attempts

A High Severity Finding is generated for investigation.

---

## 🐍 Python Integration

Later in this journey, GuardDuty will be automated using:

- Python
- Boto3
- Security Reports
- Automated Threat Detection
- CSV Export

---

## 📁 Files

- guardduty_notes.md
- interview_questions.md
- README.md

---

## 🚀 Next Topic

AWS Security Hub