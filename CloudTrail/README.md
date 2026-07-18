# Day 14 - AWS CloudTrail

## 📖 Overview

AWS CloudTrail is a logging and auditing service that records API activity within an AWS account. It helps organizations monitor user actions, investigate security incidents, and meet compliance requirements.

CloudTrail acts as the "CCTV Camera" of AWS by recording who performed an action, when it occurred, from where it originated, and whether the action was successful.

---

## 🎯 Learning Objectives

- Understand AWS CloudTrail
- Learn Management Events and Data Events
- Understand CloudTrail Event History
- Learn CloudTrail use cases in Cloud Security
- Understand how CloudTrail supports Incident Response
- Learn how Python (Boto3) interacts with CloudTrail

---

## 📚 Topics Covered

- What is AWS CloudTrail
- CloudTrail Architecture
- Management Events
- Data Events
- Event History
- CloudTrail vs CloudWatch
- Security Monitoring
- Incident Response
- Compliance
- CloudTrail with Python (Boto3)

---

## 🏗 Architecture

User
↓
AWS API Call
↓
CloudTrail
↓
Event Log
↓
Security Team / SOC / SIEM

---

## 🔒 Cloud Security Applications

- Security Auditing
- Incident Investigation
- Compliance Reporting
- User Activity Monitoring
- Change Tracking
- Threat Hunting

---

## 💼 Real-world Example

A production EC2 instance is unexpectedly terminated.

CloudTrail helps identify:

- Who terminated it
- When it happened
- Source IP Address
- AWS Region
- Whether the request succeeded

---

## 🐍 Python Integration

Later in this journey, this service will be automated using:

- Python
- Boto3
- CSV Reporting
- Security Automation

---

## 📁 Files

- cloudtrail_notes.md
- interview_questions.md
- README.md

---

## 🚀 Next Topic

Amazon CloudWatch