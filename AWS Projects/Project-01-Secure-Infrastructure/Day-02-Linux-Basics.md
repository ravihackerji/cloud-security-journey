# Day 02 - EC2 Launch, SSH Access & Linux Basics

## Objective

The goal of Day 2 was to launch an Amazon EC2 instance inside a secure VPC, configure network security using Security Groups, connect securely using SSH, and learn the basic Linux commands required for cloud administration.

---

# Architecture

```
My Laptop
     │
     ▼
Internet
     │
     ▼
Internet Gateway
     │
     ▼
Public Route Table
     │
     ▼
Public Subnet
     │
     ▼
Security Group
     │
     ▼
EC2 Instance (Amazon Linux 2023)
```

---

# AWS Services Used

- Amazon EC2
- Amazon VPC
- Public Subnet
- Internet Gateway
- Route Table
- Security Group
- SSH
- Amazon Linux 2023

---

# EC2 Launch Configuration

| Setting | Value |
|----------|-------|
| Instance Name | Public-Server |
| Operating System | Amazon Linux 2023 |
| Instance Type | t3.micro |
| VPC | Secure-VPC |
| Subnet | Public-Subnet-1 |
| Public IP | Enabled |
| Storage | 8 GB gp3 |
| Key Pair | CloudSecurityKey.pem |
| Security Group | Public-Server-SG |

---

# Security Group Configuration

## Inbound Rules

| Protocol | Port | Source | Purpose |
|----------|------|---------|---------|
| SSH | 22 | My IP | Secure remote administration |

## Outbound Rules

Default: Allow All

---

# Why "My IP" Instead of Anywhere?

Using **My IP** ensures that only my current public IP address can access the server through SSH.

This follows the Principle of Least Privilege and reduces the attack surface.

Avoid using:

```
0.0.0.0/0
```

for SSH unless absolutely necessary.

---

# SSH Connection Process

AWS generated an RSA key pair.

Downloaded key:

```
CloudSecurityKey.pem
```

Connection command:

```bash
ssh -i "CloudSecurityKey.pem" ec2-user@<Public-IP>
```

Authentication Flow:

```
Laptop
   │
SSH Client
   │
Internet
   │
Internet Gateway
   │
Public Route Table
   │
Public Subnet
   │
Security Group
   │
EC2 Instance
```

---

# Linux Commands Learned

## 1. whoami

```bash
whoami
```

Purpose:

Displays the currently logged-in Linux user.

Expected Output:

```
ec2-user
```

---

## 2. pwd

```bash
pwd
```

Purpose:

Displays the current working directory.

Expected Output:

```
/home/ec2-user
```

---

## 3. ls

```bash
ls
```

Purpose:

Lists files and folders in the current directory.

---

## 4. ls -la

```bash
ls -la
```

Purpose:

Shows all files, including hidden files, with detailed information.

---

## 5. cat /etc/os-release

```bash
cat /etc/os-release
```

Purpose:

Displays operating system information.

Expected Output:

Amazon Linux 2023

---

## 6. uname -a

```bash
uname -a
```

Purpose:

Displays Linux kernel version and system architecture.

---

## 7. df -h

```bash
df -h
```

Purpose:

Displays disk usage in human-readable format.

---

## 8. free -h

```bash
free -h
```

Purpose:

Displays RAM usage.

---

## 9. lscpu

```bash
lscpu
```

Purpose:

Displays CPU architecture and hardware information.

---

## 10. ip addr

```bash
ip addr
```

Purpose:

Displays network interfaces and private IP address.

---

# Key Concepts Learned

## EC2

Amazon Elastic Compute Cloud (EC2) is a virtual server running in AWS.

---

## Public IP

Used for communication over the Internet.

---

## Private IP

Used only within the VPC for internal communication.

---

## Security Group

A stateful virtual firewall attached to AWS resources.

Allows only authorized traffic.

---

## Route Table

Defines where network traffic should be forwarded.

```
0.0.0.0/0
        │
        ▼
Internet Gateway
```

---

## Internet Gateway

Allows communication between the VPC and the Internet.

---

# Security Best Practices

- Use Security Groups instead of opening all ports.
- Restrict SSH access to My IP.
- Never upload the private key (.pem) to GitHub.
- Stop EC2 instances after use to minimize costs.
- Use Amazon Linux official AMIs.
- Follow the Principle of Least Privilege.

---

# Challenges Faced

- SSH private key permission issues on Windows.
- Fixed Windows file permissions using `icacls`.
- Successfully established an SSH connection to the EC2 instance.

---

# Skills Gained

- Launching EC2 instances
- Configuring Security Groups
- Connecting via SSH
- Understanding Linux basics
- Working with AWS networking
- Managing SSH keys securely

---

# Interview Questions

## What is EC2?

EC2 is a scalable virtual machine service provided by AWS.

---

## Difference between Public IP and Private IP?

Public IP:

- Accessible from the Internet.

Private IP:

- Accessible only within the VPC.

---

## What is a Security Group?

A stateful firewall attached to AWS resources that controls inbound and outbound traffic.

---

## Why use My IP instead of Anywhere?

It limits SSH access to only my current IP address, improving security.

---

## What does SSH use by default?

Port:

```
22
```

---

## What command displays the current user?

```bash
whoami
```

---

## What command displays the current directory?

```bash
pwd
```

---

## What command displays the Linux version?

```bash
cat /etc/os-release
```

---

## Summary

Today I successfully:

- Built a secure EC2 environment.
- Configured Security Groups.
- Connected securely using SSH.
- Explored Linux fundamentals.
- Learned how EC2 networking works.
- Understood secure remote administration.
- Practiced cloud security best practices.

This forms the foundation for future Cloud Security and DevSecOps projects.