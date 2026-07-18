# AWS CloudTrail Notes

## What is AWS CloudTrail?

AWS CloudTrail is a logging and auditing service that records API calls made within an AWS account.

It provides visibility into account activity for governance, compliance, operational auditing, and security analysis.

---

# Why CloudTrail is Important

- Tracks all AWS API calls
- Helps investigate security incidents
- Detects unauthorized changes
- Provides audit logs
- Supports compliance standards

---

# Information Recorded by CloudTrail

- Event Name
- Event Time
- IAM User or Role
- AWS Service
- Source IP Address
- AWS Region
- Request Parameters
- Response Elements
- Success or Failure Status

---

# Types of Events

## 1. Management Events

These record operations performed on AWS resources.

Examples:

- CreateUser
- DeleteUser
- CreateBucket
- StartInstances
- StopInstances
- AttachRolePolicy
- CreateSecurityGroup

These are enabled by default.

---

## 2. Data Events

These record operations performed on data stored inside AWS services.

Examples:

Amazon S3

- GetObject
- PutObject
- DeleteObject

AWS Lambda

- InvokeFunction

Data Events provide detailed visibility but may increase logging costs.

---

# Event History

CloudTrail stores recent management events that can be searched by:

- Event Name
- Username
- Resource Name
- AWS Service
- Time
- Event Source

---

# CloudTrail Use Cases

- Security Monitoring
- Incident Response
- Compliance Auditing
- IAM Activity Review
- Change Tracking
- Forensic Investigation

---

# CloudTrail vs CloudWatch

CloudTrail

- Records AWS API activity
- Used for auditing
- Answers "Who did what?"

CloudWatch

- Monitors logs and metrics
- Used for monitoring
- Answers "What is happening?"

---

# Security Best Practices

- Enable CloudTrail in all Regions.
- Protect CloudTrail logs.
- Store logs securely in Amazon S3.
- Restrict access to logs.
- Monitor unusual API activity.
- Integrate CloudTrail with Security Hub and GuardDuty.

---

# Real Incident Example

Situation:

An S3 bucket was accidentally deleted.

Investigation Steps:

1. Search DeleteBucket event.
2. Identify IAM User.
3. Check source IP.
4. Verify event time.
5. Review related activities.

CloudTrail provides all these details.

---

# Key Points

- CloudTrail records AWS API calls.
- Used for auditing and investigations.
- Supports compliance.
- Essential for Cloud Security Engineers.
- Frequently used with Python and Boto3.
