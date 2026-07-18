# Amazon GuardDuty Interview Questions

## Beginner Level

### 1. What is Amazon GuardDuty?

Answer:

Amazon GuardDuty is a managed threat detection service that continuously monitors AWS environments for suspicious or malicious activity using machine learning, anomaly detection, and AWS threat intelligence.

---

### 2. Does GuardDuty require manual infrastructure management?

Answer:

No. It is a fully managed AWS service.

---

### 3. What data sources does GuardDuty analyze?

Answer:

- AWS CloudTrail
- VPC Flow Logs
- DNS Logs
- EKS Audit Logs
- Amazon S3 Protection

---

### 4. What is a GuardDuty Finding?

Answer:

A Finding is a security alert generated when GuardDuty detects suspicious or malicious activity.

---

### 5. What information does a Finding include?

Answer:

- Finding ID
- Threat Type
- Severity
- Resource
- Region
- Timestamp
- Description
- Recommended Action

---

## Intermediate Level

### 6. Name five threats detected by GuardDuty.

Answer:

- Cryptocurrency Mining
- Malware Communication
- Port Scanning
- Stolen Credentials
- Data Exfiltration

---

### 7. Does GuardDuty block attacks?

Answer:

No. GuardDuty detects and reports suspicious activity. Automated responses can be implemented using services like EventBridge and AWS Lambda.

---

### 8. What are the GuardDuty severity levels?

Answer:

- Low
- Medium
- High
- Critical

---

### 9. How does GuardDuty support Incident Response?

Answer:

It provides detailed findings that help responders identify threats, affected resources, and recommended actions.

---

### 10. Which AWS service centralizes GuardDuty findings?

Answer:

AWS Security Hub.

---

## Advanced Level

### 11. An EC2 instance starts communicating with a known malicious IP address. Which AWS service detects it?

Answer:

Amazon GuardDuty.

---

### 12. An attacker logs into AWS using stolen access keys from another country. Which service identifies this suspicious behavior?

Answer:

Amazon GuardDuty.

---

### 13. Which AWS service records the API calls associated with the suspicious activity?

Answer:

AWS CloudTrail.

---

### 14. How can GuardDuty findings trigger automated remediation?

Answer:

By integrating GuardDuty with Amazon EventBridge to invoke AWS Lambda, send Amazon SNS notifications, or start AWS Systems Manager Automation workflows.

---

### 15. How can GuardDuty be automated using Python?

Answer:

Using Boto3 to:

- Retrieve findings
- Filter High and Critical findings
- Generate security reports
- Export findings to CSV
- Send alerts to security teams