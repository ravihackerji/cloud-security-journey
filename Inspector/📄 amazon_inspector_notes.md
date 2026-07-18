# Amazon Inspector Notes

## What is Amazon Inspector?

Amazon Inspector is a managed vulnerability assessment service that continuously scans AWS workloads for software vulnerabilities and unintended network exposure.

It helps organizations identify security weaknesses before attackers exploit them.

---

# Why Amazon Inspector is Important

- Detects software vulnerabilities
- Improves security posture
- Supports compliance
- Helps prioritize remediation
- Reduces attack surface
- Supports DevSecOps practices

---

# Resources Scanned by Amazon Inspector

## 1. Amazon EC2

Inspector scans EC2 instances for:

- Missing security patches
- Operating system vulnerabilities
- Installed software vulnerabilities
- Network exposure

---

## 2. Amazon ECR

Inspector scans container images for:

- Vulnerable packages
- Outdated software
- Known CVEs

---

## 3. AWS Lambda

Inspector scans Lambda functions for:

- Vulnerable dependencies
- Outdated libraries
- Known software vulnerabilities

---

# What is CVE?

CVE (Common Vulnerabilities and Exposures) is a globally recognized identifier assigned to publicly disclosed security vulnerabilities.

Example:

CVE-2025-12345

---

# What is CVSS?

CVSS (Common Vulnerability Scoring System) measures the severity of a vulnerability.

Severity Levels

Low

0.1 – 3.9

Medium

4.0 – 6.9

High

7.0 – 8.9

Critical

9.0 – 10.0

---

# Inspector Findings

Each finding contains:

- Finding ID
- Resource Name
- Resource Type
- CVE ID
- Severity
- CVSS Score
- Description
- Recommended Remediation
- Detection Time

---

# Continuous Scanning

Inspector continuously scans supported AWS resources.

Example:

New EC2 Instance

↓

Automatic Scan

↓

Critical CVE Found

↓

Finding Generated

↓

Security Hub Updated

---

# Cloud Security Use Cases

- Vulnerability Assessment
- Patch Management
- Compliance Monitoring
- DevSecOps
- Container Security
- Risk Prioritization
- Security Audits

---

# Integration with AWS Services

Amazon Inspector integrates with:

- AWS Security Hub
- Amazon EventBridge
- AWS Systems Manager
- Amazon ECR
- Amazon CloudWatch
- AWS Organizations

---

# Security Best Practices

- Enable Inspector in all Regions.
- Review Critical findings immediately.
- Patch vulnerable software promptly.
- Scan container images before deployment.
- Integrate with Security Hub.
- Automate notifications using EventBridge.

---

# Real Incident Example

Situation:

An EC2 instance is running a vulnerable version of Apache.

Amazon Inspector

↓

Detects CVE

↓

Critical Finding

↓

Security Hub

↓

Security Team

↓

Patch Applied

↓

Rescan

↓

Finding Resolved

---

# GuardDuty vs Amazon Inspector

GuardDuty

- Detects active threats
- Uses CloudTrail, DNS Logs, VPC Flow Logs
- Detects suspicious behavior

Amazon Inspector

- Detects vulnerabilities
- Scans EC2, ECR, Lambda
- Detects software weaknesses

---

# Key Points

- Amazon Inspector is AWS's vulnerability assessment service.
- Continuously scans EC2, ECR, and Lambda.
- Detects vulnerabilities using CVEs.
- Uses CVSS to prioritize risk.
- Generates findings with remediation guidance.
- Integrates with Security Hub for centralized management.