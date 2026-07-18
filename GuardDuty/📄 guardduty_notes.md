# Amazon GuardDuty Notes

## What is Amazon GuardDuty?

Amazon GuardDuty is a managed threat detection service that continuously analyzes AWS account activity to identify suspicious or malicious behavior.

It uses Machine Learning, anomaly detection, and AWS threat intelligence to generate security findings.

---

# Why GuardDuty is Important

- Detects cyber threats automatically
- Monitors AWS account activity
- Detects compromised credentials
- Identifies malware communication
- Supports Incident Response
- Improves cloud security posture

---

# Data Sources Used by GuardDuty

## 1. AWS CloudTrail

Monitors:

- API Calls
- IAM Activity
- Console Logins
- Account Changes

---

## 2. VPC Flow Logs

Monitors:

- Network Traffic
- Source IP
- Destination IP
- Ports
- Protocols

---

## 3. DNS Logs

Monitors:

- DNS Requests
- Suspicious Domains
- Malware Communication
- Command-and-Control (C2) Servers

---

## 4. EKS Audit Logs

Monitors:

- Kubernetes API Activity
- Cluster Administration
- Suspicious Kubernetes Actions

---

## 5. Amazon S3 Protection

Detects:

- Unusual Bucket Access
- Data Downloads
- Credential Misuse
- Data Exfiltration Attempts

---

# Threats Detected by GuardDuty

- Compromised IAM Users
- Stolen Access Keys
- Cryptocurrency Mining
- Port Scanning
- Brute Force Attacks
- Malware Communication
- Data Exfiltration
- Privilege Escalation
- Unusual Geographic Logins
- Suspicious API Calls

---

# GuardDuty Findings

A Finding is a security alert generated when suspicious activity is detected.

Each Finding contains:

- Finding ID
- Threat Type
- Severity
- Resource
- AWS Region
- Account ID
- Timestamp
- Description
- Recommended Action

---

# Severity Levels

## Low

Minor suspicious activity.

Requires monitoring.

---

## Medium

Potential security issue.

Should be investigated.

---

## High

Serious security threat.

Immediate investigation required.

---

## Critical

Severe compromise.

Immediate response and containment required.

---

# Cloud Security Use Cases

- Detect Compromised Accounts
- Detect Malware
- Detect Data Theft
- Detect Insider Threats
- Monitor AWS Accounts
- SOC Monitoring
- Incident Response
- Threat Hunting

---

# Integration with AWS Services

GuardDuty integrates with:

- AWS Security Hub
- AWS Config
- CloudTrail
- CloudWatch
- EventBridge
- AWS Lambda
- Amazon SNS

---

# Security Best Practices

- Enable GuardDuty in all AWS Regions.
- Review findings regularly.
- Investigate High and Critical findings immediately.
- Integrate GuardDuty with Security Hub.
- Enable EventBridge for automated responses.
- Use IAM least privilege to reduce risk.

---

# Real Incident Example

Situation:

A compromised EC2 instance starts communicating with a known malicious IP.

GuardDuty Process:

Network Activity

↓

Threat Intelligence Match

↓

High Severity Finding

↓

Security Hub

↓

SOC Investigation

↓

Incident Response

---

# GuardDuty vs Other AWS Services

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

- Detects suspicious behavior
- Answers: Is this activity malicious?

---

# Key Points

- GuardDuty is AWS's threat detection service.
- Uses Machine Learning and threat intelligence.
- Generates security findings.
- Detects compromised credentials and malware.
- Integrates with Security Hub and EventBridge.
- Essential for Cloud Security Engineers.