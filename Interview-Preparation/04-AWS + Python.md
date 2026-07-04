# Interview Questions – AWS Global Infrastructure & IAM

---

# Beginner Level

## 1. What is AWS?

**Answer:**

AWS (Amazon Web Services) is a cloud computing platform that provides on-demand services such as computing, storage, networking, databases, security, and monitoring over the internet.

---

## 2. What is Cloud Computing?

**Answer:**

Cloud computing is the delivery of computing resources such as servers, storage, databases, networking, and software over the internet on a pay-as-you-go basis.

---

## 3. What is an AWS Region?

**Answer:**

An AWS Region is a geographic area that contains multiple isolated Availability Zones where AWS provides cloud services.

Example:

- us-east-1
- ap-south-1
- eu-west-1

---

## 4. What is an Availability Zone (AZ)?

**Answer:**

An Availability Zone is one or more physically separate data centers within an AWS Region that provide high availability and fault tolerance.

---

## 5. What is an Edge Location?

**Answer:**

An Edge Location is a global site used by AWS services such as Amazon CloudFront to cache and deliver content closer to users, reducing latency.

---

## 6. What is IAM?

**Answer:**

IAM (Identity and Access Management) is an AWS service used to securely manage users, groups, roles, permissions, authentication, and authorization.

---

## 7. Is IAM a Regional or Global Service?

**Answer:**

IAM is a **Global Service**.

One IAM configuration can be used across all AWS Regions in the account.

---

# Intermediate Level

## 8. Why does AWS have multiple Regions?

**Answer:**

AWS has multiple Regions to:

- Reduce latency
- Improve disaster recovery
- Meet compliance requirements
- Increase availability

---

## 9. Why are multiple Availability Zones important?

**Answer:**

Availability Zones provide:

- High Availability
- Fault Tolerance
- Business Continuity
- Load Distribution

If one AZ fails, workloads can continue in another AZ.

---

## 10. Difference Between Region and Availability Zone?

| Region | Availability Zone |
|---------|-------------------|
| Geographic location | One or more isolated data centers |
| Contains multiple AZs | Belongs to one Region |
| Used for global deployment | Used for high availability |

---

## 11. Why is IAM important?

**Answer:**

IAM controls who can access AWS resources and what actions they are allowed to perform.

It protects cloud resources from unauthorized access.

---

## 12. What are the main IAM components?

**Answer:**

- Users
- Groups
- Roles
- Policies
- MFA
- Access Keys
- Password Policies

---

## 13. What is Authentication?

**Answer:**

Authentication verifies the identity of a user or application.

Examples:

- Username
- Password
- MFA
- Access Keys

---

## 14. What is Authorization?

**Answer:**

Authorization determines what actions an authenticated user or application is allowed to perform.

---

## 15. Difference Between Authentication and Authorization?

| Authentication | Authorization |
|----------------|---------------|
| Verifies identity | Verifies permissions |
| Happens first | Happens after authentication |
| "Who are you?" | "What can you do?" |

---

## 16. What is the Principle of Least Privilege?

**Answer:**

The Principle of Least Privilege means granting only the minimum permissions required to perform a specific task.

It reduces the risk of accidental or malicious actions.

---

# Advanced Level

## 17. Why is IAM called the foundation of AWS Security?

**Answer:**

Every AWS service relies on IAM for authentication and authorization.

Without IAM, AWS cannot securely determine who is making requests or what actions they are permitted to perform.

---

## 18. How does IAM relate to Boto3?

**Answer:**

Boto3 authenticates using IAM credentials or IAM Roles.

IAM determines which AWS API operations the Python script is authorized to perform.

---

## 19. Why is choosing the correct Region important?

**Answer:**

Choosing the correct Region affects:

- Latency
- Compliance
- Data Residency
- Disaster Recovery
- Cost
- Service Availability

---

## 20. Why should applications be deployed across multiple Availability Zones?

**Answer:**

Deploying across multiple AZs increases availability and resilience because the application can continue running if one AZ becomes unavailable.

---

# Cloud Security Interview Questions

## 21. Why is IAM important for Cloud Security Engineers?

**Answer:**

IAM helps Cloud Security Engineers:

- Manage user identities
- Control permissions
- Enforce least privilege
- Audit user activity
- Secure AWS resources
- Investigate security incidents

---

## 22. How does IAM improve security?

**Answer:**

IAM improves security by:

- Authenticating users
- Authorizing actions
- Supporting MFA
- Applying least privilege
- Providing centralized access control

---

## 23. Why should every employee have a separate IAM User?

**Answer:**

Separate IAM Users provide:

- Individual accountability
- Easier auditing
- Better permission management
- Improved security
- Easier access revocation

---

## 24. Give examples of IAM use cases.

**Answer:**

- Managing developer access
- Granting EC2 permissions
- Restricting S3 bucket access
- Enabling MFA
- Creating temporary access using IAM Roles

---

## 25. Why is High Availability important?

**Answer:**

High Availability ensures applications remain accessible even if one Availability Zone experiences a failure.

---

# Scenario-Based Questions

## 26. A company has deployed all production servers in a single Availability Zone. What is the risk?

**Answer:**

If that Availability Zone fails due to a power, network, or hardware issue, all production services become unavailable.

Deploying across multiple AZs reduces this risk.

---

## 27. A company stores customer data in a Region outside its legal jurisdiction. Why could this be a problem?

**Answer:**

It may violate data residency or regulatory requirements such as GDPR or local government policies.

---

## 28. An employee accidentally receives AdministratorAccess when they only need read-only access. Which security principle has been violated?

**Answer:**

The Principle of Least Privilege.

Users should only receive the permissions required to perform their job.

---

## 29. Your Python Boto3 script returns "Access Denied". What would you check first?

**Answer:**

- IAM permissions
- Attached IAM Policy
- IAM Role or User
- Correct AWS credentials
- Region configuration

---

## 30. Why is IAM required before learning Boto3?

**Answer:**

Boto3 communicates with AWS APIs using IAM credentials.

Without proper IAM permissions, AWS will deny requests, making automation impossible.

---

# HR Interview Question

## Why is IAM considered one of the most important AWS services?

**Answer:**

IAM is responsible for controlling access to every AWS resource. It ensures that only authorized users and applications can perform approved actions, making it the foundation of AWS security.

---

# Quick Revision

| Topic | Remember |
|--------|----------|
| AWS | Cloud Computing Platform |
| Region | Geographic location |
| Availability Zone | Isolated data center(s) within a Region |
| Edge Location | Content delivery site |
| IAM | Identity and Access Management |
| Authentication | Verify identity |
| Authorization | Verify permissions |
| Least Privilege | Minimum required permissions |
| High Availability | Multi-AZ deployment |
| Boto3 | AWS SDK for Python |