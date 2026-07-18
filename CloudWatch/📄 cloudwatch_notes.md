# Amazon CloudWatch Notes

## What is Amazon CloudWatch?

Amazon CloudWatch is a monitoring and observability service that collects metrics, logs, and events from AWS resources and applications.

It provides real-time visibility into the health and performance of AWS infrastructure.

---

# Why CloudWatch is Important

- Monitors AWS resources
- Detects performance issues
- Generates alerts
- Collects logs
- Supports troubleshooting
- Improves availability
- Enhances security monitoring

---

# CloudWatch Components

## 1. Metrics

Metrics are numerical measurements collected over time.

Examples:

EC2

- CPU Utilization
- Network In
- Network Out
- Disk Read
- Disk Write

Lambda

- Invocations
- Errors
- Duration
- Throttles

---

## 2. Logs

CloudWatch Logs collect:

- Application Logs
- System Logs
- Lambda Logs
- EC2 Logs
- VPC Flow Logs

These logs help troubleshoot and investigate problems.

---

## 3. Alarms

CloudWatch Alarms monitor metrics.

When a threshold is crossed, CloudWatch performs an action.

Example:

CPU > 90%

↓

Alarm

↓

SNS Email

↓

Administrator

---

## 4. Dashboards

Dashboards display multiple metrics on one screen.

Examples:

- CPU Usage
- Memory Usage
- Network Traffic
- Error Rate
- Storage Usage

---

## 5. EventBridge

Amazon EventBridge (formerly CloudWatch Events) responds automatically to AWS events.

Example:

EC2 Instance Stops

↓

EventBridge

↓

Lambda Function

↓

Send Email

---

# CloudWatch vs CloudTrail

CloudWatch

- Monitoring
- Metrics
- Logs
- Alarms
- Dashboards
- Performance

CloudTrail

- API Logs
- Auditing
- Compliance
- User Activity
- Security Investigation

---

# Cloud Security Use Cases

- Detect High CPU Usage
- Detect Service Failures
- Monitor Login Activity
- Monitor Network Traffic
- Generate Security Alerts
- Analyze Logs
- Detect Resource Failures

---

# Security Best Practices

- Configure CloudWatch Alarms.
- Monitor critical resources.
- Store logs securely.
- Review logs regularly.
- Use dashboards for visibility.
- Integrate with SNS notifications.

---

# Real Incident Example

Situation:

Production server CPU reaches 98%.

CloudWatch Process:

Monitor CPU

↓

Threshold Exceeded

↓

Alarm Triggered

↓

SNS Notification

↓

Administrator Investigation

↓

CloudTrail Review

↓

Root Cause Found

---

# Key Points

- CloudWatch monitors AWS resources.
- Metrics represent numerical values.
- Logs store application activity.
- Alarms notify administrators.
- Dashboards provide real-time visibility.
- EventBridge enables automation.
- CloudWatch is essential for monitoring.