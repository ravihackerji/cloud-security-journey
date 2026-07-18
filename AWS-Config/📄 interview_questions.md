# AWS Config Interview Questions

## Beginner Level

### 1. What is AWS Config?

Answer:

AWS Config is a service that continuously records AWS resource configurations, tracks changes, and evaluates compliance using Config Rules.

---

### 2. What is a Configuration Item (CI)?

Answer:

A Configuration Item is a snapshot of an AWS resource's configuration at a specific point in time.

---

### 3. Why is AWS Config important?

Answer:

It helps monitor configuration changes, detect misconfigurations, maintain compliance, and investigate security incidents.

---

### 4. What is Configuration History?

Answer:

Configuration History is a timeline of changes made to AWS resource configurations.

---

### 5. What are AWS Config Rules?

Answer:

AWS Config Rules evaluate whether AWS resources comply with defined security or operational requirements.

---

## Intermediate Level

### 6. What is the difference between Managed Rules and Custom Rules?

Answer:

Managed Rules are predefined by AWS and require minimal setup.

Custom Rules are created by users, often with AWS Lambda, to enforce organization-specific policies.

---

### 7. Give examples of AWS Managed Rules.

Answer:

- root-account-mfa-enabled
- encrypted-volumes
- restricted-ssh
- iam-password-policy
- s3-bucket-public-read-prohibited

---

### 8. Can AWS Config detect if an S3 bucket becomes public?

Answer:

Yes. AWS Config records the configuration change and can evaluate it against a rule that prohibits public access.

---

### 9. Does AWS Config automatically fix non-compliant resources?

Answer:

No. AWS Config detects and reports non-compliance. Automated remediation can be implemented separately using services like AWS Systems Manager Automation or AWS Lambda.

---

### 10. Which AWS resources can AWS Config monitor?

Answer:

Examples include:

- EC2
- S3
- IAM
- VPC
- Security Groups
- RDS
- EBS
- Load Balancers

---

## Advanced Level

### 11. A Security Group suddenly allows SSH from 0.0.0.0/0. Which AWS service detects the configuration change?

Answer:

AWS Config.

---

### 12. Which AWS service identifies who changed the Security Group?

Answer:

AWS CloudTrail.

---

### 13. How does AWS Config help during compliance audits?

Answer:

It continuously evaluates resources against compliance rules and provides historical records of configuration changes, making it easier to demonstrate adherence to security standards.

---

### 14. Can AWS Config integrate with other AWS security services?

Answer:

Yes. It integrates with AWS Security Hub, Amazon EventBridge, AWS Systems Manager, AWS Lambda, and Amazon SNS for monitoring, reporting, and automated remediation.

---

### 15. How can AWS Config be automated using Python?

Answer:

Using Boto3 to:

- Retrieve compliance results
- List non-compliant resources
- Query configuration history
- Generate compliance reports
- Automate security audits
