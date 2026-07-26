# AWS Lambda & Boto3 Assignments

This repository contains my AWS Serverless Automation assignments developed using **AWS Lambda**, **Python 3.12**, and **Boto3**.

These assignments demonstrate automation of common AWS administration tasks using event-driven architecture and AWS managed services.

---

## Assignments Completed

### Assignment 1 - Automated S3 Bucket Cleanup
**Objective:** Delete S3 objects older than 30 days using AWS Lambda and Boto3.

**AWS Services Used**
- Amazon S3
- AWS Lambda
- IAM
- Amazon EventBridge
- Amazon CloudWatch

---

### Assignment 2 - Automated EBS Snapshot Creation and Cleanup
**Objective:** Automatically create EBS snapshots and delete snapshots older than the retention period.

**AWS Services Used**
- Amazon EC2
- Amazon EBS
- AWS Lambda
- IAM
- Amazon EventBridge
- Amazon CloudWatch

---

### Assignment 3 - Auto-Tag EC2 Instances on Launch
**Objective:** Automatically tag newly launched EC2 instances using Amazon EventBridge and AWS Lambda.

**AWS Services Used**
- Amazon EC2
- AWS Lambda
- IAM
- Amazon EventBridge
- Amazon CloudWatch

---

### Assignment 6 - Audit S3 Buckets for Public Access
**Objective:** Detect publicly accessible S3 buckets and send email notifications using Amazon SNS.

**AWS Services Used**
- Amazon S3
- Amazon SNS
- AWS Lambda
- IAM
- Amazon EventBridge
- Amazon CloudWatch

---

## Repository Structure

```
AWS-Lambda-Boto3-Assignments
│
├── Assignment1-S3Cleanup
├── Assignment2-EBSSnapshot
├── Assignment3-AutoTagEC2
├── Assignment6-S3PublicAudit
└── README.md
```

---

## Technologies Used

- Python 3.12
- AWS Lambda
- Boto3
- Amazon S3
- Amazon EC2
- Amazon EBS
- Amazon SNS
- Amazon EventBridge
- Amazon CloudWatch
- IAM

---

## Features

- Event-driven serverless automation
- Least-privilege IAM policies
- CloudWatch logging
- Scheduled automation using EventBridge
- Email notifications using SNS
- Automated resource tagging
- Automated snapshot management
- S3 security auditing

---

## Prerequisites

- AWS Account
- Python 3.12
- AWS Lambda
- IAM Roles
- Boto3
- Amazon EventBridge
- Amazon SNS

---

## Author

**Gayatri Sonar**

GitHub: https://github.com/gauryd

---

## Note

These assignments were implemented for learning AWS Serverless Automation using Lambda and Boto3. All resources were cleaned up after testing to avoid unnecessary AWS charges.
