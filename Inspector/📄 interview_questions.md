# Amazon Inspector Interview Questions

## Beginner Level

### 1. What is Amazon Inspector?

**Answer:**

Amazon Inspector is a managed AWS service that continuously scans EC2 instances, Amazon ECR container images, and AWS Lambda functions for software vulnerabilities and unintended network exposure.

---

### 2. What AWS resources can Amazon Inspector scan?

**Answer:**

- Amazon EC2
- Amazon ECR Container Images
- AWS Lambda Functions

---

### 3. What is a CVE?

**Answer:**

A CVE (Common Vulnerabilities and Exposures) is a standardized identifier for a publicly known security vulnerability.

---

### 4. What is CVSS?

**Answer:**

CVSS (Common Vulnerability Scoring System) is a standardized framework used to measure the severity of security vulnerabilities.

---

### 5. Does Amazon Inspector automatically fix vulnerabilities?

**Answer:**

No. It detects vulnerabilities and provides remediation recommendations, but customers must apply patches or implement the recommended fixes.

---

## Intermediate Level

### 6. What information is included in an Inspector finding?

**Answer:**

- Resource
- CVE ID
- Severity
- CVSS Score
- Description
- Recommendation
- Detection Time

---

### 7. What is continuous scanning?

**Answer:**

Continuous scanning means Inspector automatically monitors supported AWS resources for newly discovered vulnerabilities without requiring manual scans.

---

### 8. How does Amazon Inspector support DevSecOps?

**Answer:**

It identifies vulnerabilities early in the development and deployment lifecycle, enabling teams to fix issues before production.

---

### 9. Which AWS service centralizes Amazon Inspector findings?

**Answer:**

AWS Security Hub.

---

### 10. Which AWS service can automate responses to Inspector findings?

**Answer:**

Amazon EventBridge can trigger AWS Lambda, Amazon SNS, or AWS Systems Manager Automation workflows.

---

## Advanced Level

### 11. A container image contains a package affected by a Critical CVE. Which AWS service detects it?

**Answer:**

Amazon Inspector.

---

### 12. What is the difference between GuardDuty and Amazon Inspector?

**Answer:**

GuardDuty detects suspicious or malicious activity, while Amazon Inspector identifies software vulnerabilities and unintended network exposure.

---

### 13. How can Amazon Inspector improve compliance?

**Answer:**

It continuously identifies vulnerabilities, helping organizations maintain secure systems and satisfy compliance requirements such as PCI DSS, ISO 27001, and SOC 2.

---

### 14. How can Inspector findings be integrated into automated remediation?

**Answer:**

Using EventBridge to trigger Lambda functions, Systems Manager Automation, or notifications whenever new findings are generated.

---

### 15. How can Amazon Inspector be automated using Python?

**Answer:**

Using Boto3 to:

- Retrieve findings
- Filter Critical vulnerabilities
- Generate vulnerability reports
- Export findings to CSV
- Send alerts
- Track remediation progress