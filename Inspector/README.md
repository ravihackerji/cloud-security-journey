# Day 19 - Amazon Inspector

## 📖 Overview

Amazon Inspector is AWS's managed vulnerability assessment service that continuously scans AWS workloads for software vulnerabilities and unintended network exposure.

It automatically identifies vulnerabilities in EC2 instances, Amazon ECR container images, and AWS Lambda functions, helping organizations strengthen their security posture.

Amazon Inspector is a key service for vulnerability management and DevSecOps.

---

## 🎯 Learning Objectives

- Understand Amazon Inspector
- Learn Vulnerability Assessment
- Understand CVE and CVSS
- Learn Continuous Scanning
- Understand Inspector Findings
- Learn Integration with AWS Services
- Learn Python (Boto3) Integration

---

## 📚 Topics Covered

- Amazon Inspector
- Vulnerability Assessment
- EC2 Scanning
- Amazon ECR Scanning
- Lambda Scanning
- CVE
- CVSS
- Findings
- Continuous Scanning
- Security Monitoring

---

## 🏗 Architecture

EC2

↓

Amazon ECR

↓

Lambda

↓

Amazon Inspector

↓

Vulnerability Scan

↓

Security Findings

↓

AWS Security Hub

↓

Security Team

---

## 🔒 Cloud Security Applications

- Vulnerability Assessment
- Patch Management
- Container Security
- DevSecOps
- Compliance Auditing
- Risk Assessment

---

## 💼 Real-world Example

A company deploys a web application on Amazon EC2.

Amazon Inspector scans the instance and discovers an outdated OpenSSL package affected by a Critical CVE.

The finding is sent to AWS Security Hub, allowing the security team to prioritize remediation before attackers can exploit the vulnerability.

---

## 🐍 Python Integration

Later in this journey, Inspector will be automated using:

- Python
- Boto3
- Vulnerability Reports
- CSV Export
- Automated Notifications

---

## 📁 Files

- amazon_inspector_notes.md
- interview_questions.md
- README.md

---

## 🚀 Next Topic

AWS Key Management Service (KMS)