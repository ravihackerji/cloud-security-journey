# Amazon CloudWatch Interview Questions

## Beginner Level

### 1. What is Amazon CloudWatch?

Answer:

Amazon CloudWatch is an AWS monitoring and observability service that collects metrics, logs, and events from AWS resources and applications.

---

### 2. What are CloudWatch Metrics?

Answer:

Metrics are numerical measurements collected over time, such as CPU utilization, network traffic, request count, or latency.

---

### 3. What are CloudWatch Logs?

Answer:

CloudWatch Logs store application logs, system logs, Lambda logs, and AWS service logs for monitoring and troubleshooting.

---

### 4. What is a CloudWatch Alarm?

Answer:

A CloudWatch Alarm monitors a metric and triggers an action, such as sending a notification, when a predefined threshold is reached.

---

### 5. What is a CloudWatch Dashboard?

Answer:

A dashboard is a customizable visual interface that displays multiple metrics and alarms in a single view.

---

## Intermediate Level

### 6. Difference between CloudWatch and CloudTrail?

Answer:

CloudWatch monitors performance, metrics, logs, and operational health.

CloudTrail records AWS API calls for auditing and security investigations.

---

### 7. What is Amazon EventBridge?

Answer:

Amazon EventBridge is an event bus service that responds to AWS events and can automatically trigger services like AWS Lambda or Amazon SNS.

---

### 8. Give three CloudWatch Metrics for EC2.

Answer:

- CPU Utilization
- Network In
- Network Out

---

### 9. Why are CloudWatch Alarms important?

Answer:

They notify administrators when monitored resources exceed configured thresholds, enabling quick response to operational or security issues.

---

### 10. What actions can a CloudWatch Alarm trigger?

Answer:

- Amazon SNS notification
- AWS Lambda function
- EC2 recovery (supported scenarios)
- Auto Scaling actions

---

## Advanced Level

### 11. CPU utilization reaches 98%. Which AWS service detects it?

Answer:

Amazon CloudWatch.

---

### 12. After receiving a CPU alarm, which AWS service helps determine who modified the EC2 instance?

Answer:

AWS CloudTrail.

---

### 13. Can CloudWatch monitor custom application metrics?

Answer:

Yes. You can publish custom metrics using the CloudWatch API or AWS SDKs such as Boto3.

---

### 14. How can CloudWatch improve cloud security?

Answer:

By monitoring resource health, generating alerts for suspicious activity, collecting logs, and integrating with other AWS security services.

---

### 15. How can CloudWatch be automated with Python?

Answer:

Using Boto3 to:

- Read metrics
- Create alarms
- Publish custom metrics
- Retrieve logs
- Generate monitoring reports