# Day 15 - Amazon CloudWatch

## 📖 Overview

Amazon CloudWatch is AWS's monitoring and observability service that helps monitor AWS resources, applications, and infrastructure in real time.

It collects metrics, logs, and events, allowing engineers to detect issues, create alarms, visualize dashboards, and automate responses.

CloudWatch is one of the most important AWS services used by Cloud Engineers, DevOps Engineers, SREs, and Cloud Security Engineers.

---

## 🎯 Learning Objectives

- Understand Amazon CloudWatch
- Learn CloudWatch Metrics
- Understand CloudWatch Logs
- Learn CloudWatch Alarms
- Learn Dashboards
- Understand EventBridge Integration
- Compare CloudWatch with CloudTrail
- Learn Cloud Security monitoring

---

## 📚 Topics Covered

- Amazon CloudWatch
- Metrics
- Logs
- Alarms
- Dashboards
- EventBridge
- Monitoring
- Security Monitoring
- CloudTrail vs CloudWatch
- Python Integration

---

## 🏗 CloudWatch Architecture

AWS Resources

↓

CloudWatch

↓

Metrics
Logs
Events

↓

Alarms

↓

SNS

↓

Email / SMS / Lambda

---

## 🔒 Cloud Security Applications

- Infrastructure Monitoring
- Security Monitoring
- Performance Monitoring
- Alerting
- Incident Detection
- Operational Visibility

---

## 💼 Real-world Example

A production EC2 server reaches 95% CPU usage.

CloudWatch detects the spike, triggers an alarm, sends an SNS notification, and the operations team investigates the issue.

---

## 🐍 Python Integration

Later in this journey, CloudWatch will be automated using:

- Python
- Boto3
- CloudWatch APIs
- Alarm Automation
- Monitoring Reports

---

## 📁 Files

- cloudwatch_notes.md
- interview_questions.md
- README.md

---

## 🚀 Next Topic

AWS Config