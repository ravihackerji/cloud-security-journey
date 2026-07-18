# AWS Security Hub Notes

## What is AWS Security Hub?

AWS Security Hub is a centralized security posture management service that collects, organizes, prioritizes, and displays security findings from AWS security services and supported third-party tools.

It provides a single place to monitor the overall security posture of AWS environments.

---

# Why Security Hub is Important

- Centralizes security findings
- Improves security visibility
- Simplifies compliance monitoring
- Prioritizes security risks
- Supports incident response
- Integrates multiple AWS security services

---

# Security Findings

A Finding is a reported security issue from an AWS service or integrated security product.

Examples:

- Public S3 Bucket
- Unencrypted EBS Volume
- Root User without MFA
- Critical EC2 Vulnerability
- Overly Permissive IAM Policy
- Compromised IAM Credentials

Each finding includes:

- Finding ID
- Severity
- Resource
- Account ID
- Region
- Timestamp
- Description
- Recommendation

---

# AWS Security Standards

## 1. AWS Foundational Security Best Practices (FSBP)

AWS provides predefined security controls based on AWS best practices.

Examples:

- Enable CloudTrail
- Enable MFA for Root User
- Enable EBS Encryption
- Enable S3 Block Public Access
- Configure IAM Password Policy

---

## 2. CIS AWS Foundations Benchmark

The Center for Internet Security (CIS) Benchmark provides industry-recognized security controls.

Examples:

- Root MFA Enabled
- Logging Enabled
- Password Policy Configured
- Least Privilege IAM
- CloudTrail Enabled

---

# Security Score

Security Hub calculates a Security Score based on compliance with enabled security standards.

Example:

Security Score

85%

Passed Controls

850

Failed Controls

150

A higher score indicates better compliance and security posture.

---

# Integrations

Security Hub integrates with:

- Amazon GuardDuty
- AWS Config
- Amazon Inspector
- IAM Access Analyzer
- Amazon Macie
- AWS Firewall Manager
- AWS Audit Manager
- Third-party Security Products

---

# Automated Response

Example Workflow

GuardDuty

↓

High Severity Finding

↓

Security Hub

↓

Amazon EventBridge

↓

AWS Lambda

↓

Disable IAM User

↓

Amazon SNS Notification

↓

Security Team

---

# Cloud Security Use Cases

- Centralized Security Dashboard
- Compliance Reporting
- Security Monitoring
- Incident Response
- Threat Prioritization
- Risk Assessment
- Multi-Account Security Management

---

# Security Best Practices

- Enable Security Hub in all Regions.
- Enable AWS Foundational Security Best Practices.
- Enable CIS Benchmark.
- Review High Severity Findings daily.
- Integrate with GuardDuty and AWS Config.
- Automate responses using EventBridge and Lambda.

---

# Real Incident Example

Situation:

A compromised IAM user creates a new administrator account.

CloudTrail

↓

Records API Calls

↓

GuardDuty

↓

Detects Suspicious Activity

↓

Security Hub

↓

Displays Critical Finding

↓

EventBridge

↓

Lambda

↓

Disable User

↓

SOC Investigation

---

# AWS Security Services Comparison

CloudTrail

- Records API activity
- Answers: Who performed the action?

CloudWatch

- Monitors metrics and logs
- Answers: What is happening?

AWS Config

- Tracks configuration changes
- Answers: What changed?

GuardDuty

- Detects threats
- Answers: Is this activity malicious?

Security Hub

- Centralizes findings
- Answers: What security issues require attention?

---

# Key Points

- Security Hub is the central dashboard for AWS security.
- It aggregates findings from multiple AWS security services.
- Supports AWS Foundational Security Best Practices and CIS Benchmark.
- Provides Security Score.
- Enables centralized compliance monitoring.
- Integrates with EventBridge and Lambda for automation.
- Essential for Security Operations Centers (SOC).