# Assignment 6 - Audit S3 Buckets for Public Access

## Objective

Audit all Amazon S3 buckets for public access and send an SNS email notification whenever a public bucket is detected.

---

## AWS Services Used

- Amazon S3
- Amazon SNS
- AWS Lambda
- Amazon EventBridge
- IAM
- Amazon CloudWatch
- Python 3.12
- Boto3

---

## Architecture

EventBridge Schedule

↓

AWS Lambda

↓

Amazon S3

↓

SNS Email Notification

↓

CloudWatch Logs

---

## IAM Permissions

The Lambda execution role was configured with least-privilege permissions.

Permissions used:

- s3:ListAllMyBuckets
- s3:GetBucketPublicAccessBlock
- s3:GetBucketPolicyStatus
- s3:GetBucketAcl
- sns:Publish
- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents

---

## Implementation Steps

1. Created an SNS topic.
2. Confirmed the email subscription.
3. Created a Lambda IAM Role.
4. Added an inline IAM policy.
5. Created a Lambda function using Python 3.12.
6. Configured the SNS Topic ARN.
7. Lambda listed all S3 buckets.
8. Checked Public Access Block configuration.
9. Checked Bucket Policy Status.
10. Checked Bucket ACL.
11. Published an SNS notification when a public bucket was detected.
12. Configured EventBridge to execute the Lambda daily.

---

## Testing

Created a test bucket.

Temporarily disabled Block Public Access.

Added a public bucket policy.

Executed the Lambda.

Expected Result:

- SNS email received.
- Bucket name appeared in CloudWatch Logs.
- Public bucket detected successfully.

After testing:

- Re-enabled Block Public Access.
- Removed the public bucket policy.

---

## Output

Successfully detected public S3 buckets and generated email notifications.

---

## Discussion

AWS Config and Security Hub provide managed compliance checks for S3 security. Lambda provides greater flexibility by allowing custom validation logic, notifications, and integration with external systems such as Slack, Microsoft Teams, or ticketing platforms.

---

## Cleanup

- Removed the public bucket policy.
- Enabled Block Public Access.
- Deleted the test bucket.
- Deleted the SNS topic.
- Deleted Lambda function.
- Deleted EventBridge rule.
- Deleted IAM role.