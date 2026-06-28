# IAM Audit Report using Python

## Objective

This project simulates an AWS IAM security audit.

The script identifies users who do not have Multi-Factor Authentication (MFA) enabled and generates a separate compliance report.

---

## Technologies Used

- Python
- CSV Module

---

## Project Workflow

users.csv

↓

Read CSV File

↓

Find Users with MFA Disabled

↓

Display Summary

↓

Generate Report

---

## Input File

users.csv

Contains:

- Username
- MFA Status

---

## Output File

mfa_report.csv

Contains only users whose MFA status is Disabled.

---

## Cloud Security Use Case

Cloud Security Engineers frequently perform IAM audits to identify users without MFA.

This project demonstrates how Python can automate a basic compliance check.

---

## Future Improvements

- Read IAM users directly from AWS using Boto3.
- Export reports to Excel.
- Send email notifications.
- Generate HTML dashboards.
- Schedule daily audits.
