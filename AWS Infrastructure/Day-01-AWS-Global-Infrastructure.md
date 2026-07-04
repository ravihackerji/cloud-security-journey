# Day 13 – AWS Global Infrastructure & IAM Fundamentals

## 📅 Date

04 July 2026

---

# 🎯 Objective

Today I started my AWS Security journey by learning the foundation of AWS infrastructure and Identity & Access Management (IAM).

I explored how AWS builds its global cloud infrastructure and why IAM is considered the most important security service in AWS.

Understanding these concepts is essential before automating AWS using Python and Boto3.

---

# 📚 Topics Covered

## 1. AWS Global Infrastructure

### AWS Regions

A Region is a geographical area where AWS provides cloud services.

Examples:

- us-east-1
- us-west-2
- ap-south-1
- ap-southeast-1
- eu-west-1

---

### Availability Zones (AZs)

Each AWS Region contains multiple Availability Zones.

Benefits:

- High Availability
- Fault Tolerance
- Better Reliability

---

### Edge Locations

Edge Locations are used by services like Amazon CloudFront to deliver content closer to users, reducing latency and improving performance.

---

## Difference Between Region and Availability Zone

| Region | Availability Zone |
|---------|-------------------|
| Geographic location | Isolated data center(s) within a Region |
| Contains multiple AZs | Belongs to one Region |
| Supports global deployment | Provides fault tolerance |

---

## Why AWS Uses Multiple Regions

- Reduce latency
- Disaster recovery
- Meet compliance and data residency requirements

---

## Why AWS Uses Multiple Availability Zones

- High availability
- Fault tolerance
- Load distribution

---

# 2. AWS Identity and Access Management (IAM)

## What is IAM?

AWS IAM (Identity and Access Management) is the service used to securely manage users, permissions, authentication, and authorization within an AWS account.

---

## Why IAM Exists

IAM solves several security challenges:

- Identity Management
- Permission Management
- Accountability
- Least Privilege

---

## Authentication vs Authorization

### Authentication

Verifies **who you are**.

Examples:

- Username
- Password
- Multi-Factor Authentication (MFA)

### Authorization

Determines **what actions you are allowed to perform** after authentication.

---

## IAM Components

- Users
- Groups
- Roles
- Policies
- MFA
- Access Keys
- Password Policies

---

# ☁ Cloud Security Importance

IAM is the foundation of AWS Security because it controls access to every AWS resource.

Cloud Security Engineers use IAM to:

- Enforce least privilege
- Manage user access
- Audit permissions
- Secure cloud resources
- Monitor authentication activities

---

# 🔄 Learning Workflow

```
User

↓

IAM Authentication

↓

Authorization

↓

AWS Service

↓

Cloud Resource
```

---

# 💡 Key Takeaways

- AWS is divided into Regions.
- Each Region contains multiple Availability Zones.
- Availability Zones improve fault tolerance.
- IAM controls authentication and authorization.
- Every AWS service relies on IAM permissions.
- IAM is a global AWS service.
- Least Privilege is a fundamental security principle.

---

# 🚀 Next Learning Goals

- Root User vs IAM User
- IAM Users
- IAM Groups
- IAM Policies
- IAM Roles
- Multi-Factor Authentication (MFA)
- Access Keys
- Installing Boto3
- First Python Script with AWS

---

# 📚 Current Learning Progress

## Python for Cloud Security ✅

- JSON
- File Handling
- CSV
- Logging
- Exception Handling
- Requests
- REST APIs
- Authentication
- Environment Variables

---

## AWS Cloud Security 🚀

- AWS Introduction
- Global Infrastructure
- Regions
- Availability Zones
- Edge Locations
- IAM Introduction

---

# 🎯 Personal Reflection

Today's learning made me realize that cloud security starts with identity and access management. Before automating AWS with Python, understanding how AWS authenticates users and controls permissions is essential for building secure cloud solutions.