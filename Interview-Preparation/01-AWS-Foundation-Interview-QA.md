# AWS Cloud Security Foundation – Top Interview Questions & Answers

## 1. What is Cloud Computing?

**Answer:**

Cloud computing is the delivery of computing resources such as servers, storage, databases, networking, and software over the internet on a pay-as-you-go basis. It allows organizations to use IT resources without owning physical infrastructure.

---

## 2. What is AWS?

**Answer:**

AWS (Amazon Web Services) is Amazon's cloud computing platform that provides cloud services such as computing, storage, networking, databases, security, and monitoring.

---

## 3. What is IAM?

**Answer:**

IAM (Identity and Access Management) is the AWS service that controls who can access AWS resources and what actions they are allowed to perform.

---

## 4. What is the difference between Authentication and Authorization?

**Authentication:** Verifies the identity of a user.

**Authorization:** Determines what an authenticated user is allowed to do.

---

## 5. What is the Principle of Least Privilege?

**Answer:**

The Principle of Least Privilege means granting only the minimum permissions required to perform a task. This reduces the attack surface and limits the impact of compromised accounts.

---

## 6. What is the AWS Root User?

**Answer:**

The Root User is the first account created with an AWS account. It has unrestricted access to all AWS resources and should only be used for special administrative tasks. MFA should always be enabled.

---

## 7. Why should the Root User not be used for daily work?

**Answer:**

Because it has unrestricted permissions. If compromised, an attacker could gain complete control of the AWS account. Daily administration should be performed using IAM Users or IAM Roles.

---

## 8. What is an IAM User?

**Answer:**

An IAM User is a permanent identity created within an AWS account. It can have a username, password, access keys, and assigned permissions.

---

## 9. What is an IAM Role?

**Answer:**

An IAM Role is a set of temporary permissions that can be assumed by users, applications, or AWS services. Roles are generally preferred for applications because they use temporary credentials instead of long-term access keys.

---

## 10. What is an IAM Policy?

**Answer:**

An IAM Policy is a JSON document that defines which AWS actions are allowed or denied on specific resources.

---

## 11. What are the main parts of an IAM Policy?

**Answer:**

* Version
* Statement
* Effect
* Action
* Resource

---

## 12. What is the difference between Allow and Deny?

**Answer:**

* **Allow:** Grants permission.
* **Deny:** Blocks permission.

In AWS, **Explicit Deny always overrides Allow**.

---

## 13. What does "*" (wildcard) mean in an IAM Policy?

**Answer:**

The wildcard "*" means "all."

Examples:

* `"Action": "*"` → All actions.
* `"Resource": "*"` → All resources.

These should be used carefully because they can grant very broad permissions.

---

## 14. What is EC2?

**Answer:**

Amazon EC2 (Elastic Compute Cloud) is AWS's virtual machine service. It provides scalable compute resources in the cloud.

---

## 15. What is the difference between a Public IP and a Private IP?

**Public IP:**

Accessible over the internet.

**Private IP:**

Used for communication within a private cloud network and is not directly reachable from the internet.

---

## 16. What is Amazon S3?

**Answer:**

Amazon S3 (Simple Storage Service) is AWS's object storage service used to store files such as images, videos, backups, documents, and logs.

---

## 17. What is the difference between a Bucket and an Object?

**Bucket:**

A top-level storage container.

**Object:**

An individual file stored inside a bucket.

---

## 18. Why are Public S3 Buckets considered a security risk?

**Answer:**

A public bucket can expose sensitive company data to anyone on the internet if not properly configured. Public access should only be enabled when there is a clear business requirement.

---

## 19. What is a VPC?

**Answer:**

A Virtual Private Cloud (VPC) is an isolated virtual network in AWS where cloud resources such as EC2 instances and databases are deployed.

---

## 20. What is the difference between a Public Subnet and a Private Subnet?

**Public Subnet:**

Can host internet-facing resources if networking rules permit.

**Private Subnet:**

Used for internal resources such as databases and application backends that should not be directly accessible from the internet.

---

## 21. What is an Internet Gateway?

**Answer:**

An Internet Gateway allows communication between a VPC and the internet.

---

## 22. What is a Route Table?

**Answer:**

A Route Table contains rules that determine where network traffic is directed.

---

## 23. What is the difference between a Security Group and a Network ACL?

**Security Group:**

Acts as a virtual firewall for individual resources such as EC2 instances.

**Network ACL:**

Acts as a firewall for an entire subnet.

---

## 24. Why should databases be placed in a Private Subnet?

**Answer:**

Databases usually contain sensitive information. Placing them in a Private Subnet reduces exposure by preventing direct internet access.

---

## 25. Why are IAM Roles preferred over Access Keys for applications?

**Answer:**

IAM Roles provide temporary credentials, avoid hard-coded secrets, support automatic credential rotation, and improve overall security.

---

# Key Interview Tips

* Explain concepts in simple language first.
* Mention security best practices whenever possible.
* Emphasize the Principle of Least Privilege.
* Recommend MFA for privileged accounts.
* Prefer IAM Roles over long-term Access Keys.
* Avoid exposing databases or sensitive resources directly to the internet.

---

# Quick Revision

* Cloud Computing = IT resources delivered over the internet.
* AWS = Amazon's cloud platform.
* IAM = Identity and Access Management.
* Root User = Full account access.
* IAM Policy = JSON permissions document.
* EC2 = Virtual Machine.
* S3 = Object Storage.
* VPC = Private cloud network.
* Public Subnet = Internet-facing.
* Private Subnet = Internal-only.
* Security Group = Resource-level firewall.
* Network ACL = Subnet-level firewall.
* Least Privilege = Grant only the permissions required.
