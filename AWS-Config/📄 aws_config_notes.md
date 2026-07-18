# AWS Config Notes

## What is AWS Config?

AWS Config is a configuration management service that continuously records AWS resource configurations, tracks changes over time, and evaluates compliance against predefined or custom rules.

It helps organizations maintain security, governance, and operational best practices.

---

# Why AWS Config is Important

- Tracks configuration changes
- Detects misconfigurations
- Maintains compliance
- Improves governance
- Supports incident investigations
- Provides configuration history

---

# What AWS Config Records

AWS Config records configurations for resources such as:

- EC2 Instances
- Security Groups
- S3 Buckets
- IAM Roles
- VPCs
- Subnets
- Route Tables
- Load Balancers
- RDS Databases
- EBS Volumes

---

# Configuration Item (CI)

A Configuration Item (CI) is a snapshot of an AWS resource's configuration at a specific point in time.

Example:

EC2 Instance

- Instance ID
- Instance Type
- Security Group
- State
- Tags
- Region

Whenever a configuration changes, AWS Config creates a new Configuration Item.

---

# Configuration History

AWS Config stores historical records of resource configurations.

Example Timeline:

09:00

Security Group

Port 22 Closed

↓

11:30

Port 22 Open

↓

03:00

Port 22 Closed Again

This history allows engineers to understand exactly when and how a resource changed.

---

# Resource Relationships

AWS Config also records relationships between resources.

Example:

EC2 Instance

↓

Attached Security Group

↓

VPC

↓

Subnet

↓

EBS Volume

This helps visualize infrastructure dependencies.

---

# AWS Config Rules

Config Rules evaluate AWS resources against security and operational requirements.

Examples:

- S3 Buckets should not be public.
- Root account should have MFA enabled.
- EBS Volumes must be encrypted.
- Security Groups should not allow unrestricted SSH access.
- IAM password policy should be enabled.

---

# Managed Rules

Managed Rules are predefined compliance rules created by AWS.

Examples:

- root-account-mfa-enabled
- encrypted-volumes
- restricted-ssh
- s3-bucket-public-read-prohibited
- iam-password-policy

Advantages:

- Easy to enable
- No coding required
- Maintained by AWS

---

# Custom Rules

Custom Rules allow organizations to create their own compliance checks.

Usually implemented using AWS Lambda.

Example:

Every EC2 instance must have:

Environment = Production

If missing, AWS Config marks it as Non-Compliant.

---

# Compliance Dashboard

The AWS Config dashboard displays:

- Compliant Resources
- Non-Compliant Resources
- Rule Evaluation Results
- Configuration Timeline
- Resource Inventory

---

# Cloud Security Use Cases

- Detect Public S3 Buckets
- Detect Open Security Groups
- Monitor IAM Configuration
- Verify Encryption
- Track Resource Changes
- Support Compliance Audits
- Investigate Security Incidents

---

# Security Best Practices

- Enable AWS Config in all Regions.
- Use Managed Rules where possible.
- Create Custom Rules for organization-specific policies.
- Review Non-Compliant resources regularly.
- Integrate with Security Hub.
- Store configuration history securely.

---

# Real Incident Example

Situation:

A Security Group suddenly allows SSH from 0.0.0.0/0.

AWS Config Process:

Configuration Change

↓

Configuration Item Created

↓

Config Rule Evaluated

↓

Resource Marked Non-Compliant

↓

Security Team Investigates

↓

CloudTrail Identifies Who Made the Change

---

# AWS Config vs CloudTrail vs CloudWatch

CloudTrail

- Records API activity
- Answers: Who did it?

CloudWatch

- Monitors metrics and logs
- Answers: What is happening?

AWS Config

- Tracks configuration changes
- Answers: What changed?

---

# Key Points

- AWS Config continuously records resource configurations.
- Configuration Items are snapshots of resource states.
- Config Rules evaluate compliance.
- Managed Rules are provided by AWS.
- Custom Rules can be created using AWS Lambda.
- AWS Config is essential for governance and compliance.