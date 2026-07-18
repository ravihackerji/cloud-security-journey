# Day 16 - AWS Config

## 📖 Overview

AWS Config is a configuration management and compliance service that continuously monitors, records, and evaluates the configuration of AWS resources.

It enables organizations to track configuration changes, maintain compliance, investigate incidents, and improve cloud governance.

AWS Config is one of the most important services for Cloud Security Engineers because it provides visibility into how AWS resources change over time.

---

## 🎯 Learning Objectives

- Understand AWS Config
- Learn Configuration Items (CI)
- Learn Configuration History
- Understand Config Rules
- Learn Managed and Custom Rules
- Understand Compliance Monitoring
- Compare AWS Config with CloudTrail and CloudWatch
- Learn Python (Boto3) integration

---

## 📚 Topics Covered

- AWS Config
- Configuration Items
- Configuration History
- Resource Relationships
- Config Rules
- Managed Rules
- Custom Rules
- Compliance Dashboard
- Cloud Security Applications
- Python Integration

---

## 🏗 Architecture

AWS Resources

↓

AWS Config

↓

Configuration Items

↓

Configuration History

↓

Config Rules

↓

Compliance Dashboard

---

## 🔒 Cloud Security Applications

- Configuration Monitoring
- Compliance Auditing
- Security Governance
- Resource Change Tracking
- Detecting Misconfigurations
- Incident Investigation

---

## 💼 Real-world Example

A Security Group accidentally allows SSH (Port 22) from the entire internet.

AWS Config:

- Detects the configuration change.
- Records the previous and new configuration.
- Evaluates it against a Config Rule.
- Marks the resource as Non-Compliant.

---

## 🐍 Python Integration

Later in this journey, AWS Config will be automated using:

- Python
- Boto3
- Compliance Reports
- Security Audits
- Automated Configuration Checks

---

## 📁 Files

- aws_config_notes.md
- interview_questions.md
- README.md

---

## 🚀 Next Topic

Amazon GuardDuty