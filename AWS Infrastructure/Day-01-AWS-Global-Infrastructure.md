# AWS Global Infrastructure Notes

## 1. Five AWS Regions

| Region Name | Region Code |
|--------------|-------------|
| US East (N. Virginia) | us-east-1 |
| US West (Oregon) | us-west-2 |
| Asia Pacific (Mumbai) | ap-south-1 |
| Asia Pacific (Singapore) | ap-southeast-1 |
| Europe (Ireland) | eu-west-1 |

---

# 2. Difference Between Region and Availability Zone

| AWS Region | Availability Zone (AZ) |
|------------|--------------------------|
| A geographical area where AWS provides cloud services. | One or more isolated data centers within a Region. |
| Contains multiple Availability Zones. | Belongs to a single Region. |
| Used for global deployment and data residency. | Used for high availability and fault tolerance. |
| Example: ap-south-1 | Example: ap-south-1a |

---

# 3. Three Reasons for Multiple AWS Regions

### 1. Reduce Latency
Users can access services from the nearest Region, resulting in faster response times.

### 2. Disaster Recovery
If one Region becomes unavailable due to a major outage or natural disaster, applications and data can be recovered from another Region.

### 3. Compliance and Data Residency
Some organizations and governments require customer data to remain within a specific country or geographic location. Multiple Regions help meet these legal and regulatory requirements.

---

# 4. Three Reasons for Multiple Availability Zones

### 1. High Availability
Applications continue running even if one Availability Zone experiences a failure.

### 2. Fault Tolerance
Failures such as power outages or networking issues in one AZ do not affect other AZs in the same Region.

### 3. Load Distribution
Applications and workloads can be distributed across multiple AZs to improve reliability and performance.

---

# 5. Three Cloud Security Benefits of AWS Regions

### 1. Data Residency
Organizations can store sensitive data in specific Regions to comply with regulations such as GDPR, HIPAA, or local government policies.

### 2. Disaster Recovery
Critical workloads can be replicated across Regions, ensuring business continuity during regional failures.

### 3. Security and Compliance
AWS provides Region-specific security controls, allowing organizations to meet compliance standards while protecting data and applications.

---

# Key Takeaways

- AWS is divided into multiple Regions around the world.
- Each Region contains multiple Availability Zones.
- Availability Zones improve reliability and fault tolerance.
- Regions help reduce latency and meet compliance requirements.
- Choosing the correct Region is an important security and architectural decision.
- Boto3 requires a Region to communicate with AWS services.
