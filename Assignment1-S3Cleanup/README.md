# Assignment 1 - Automated S3 Bucket Cleanup

## Objective

Automate the deletion of S3 objects older than 30 days using AWS Lambda and Boto3.

---

## AWS Services Used

- Amazon S3
- AWS Lambda
- IAM
- Amazon EventBridge
- Amazon CloudWatch
- Python 3.12
- Boto3

---

## Architecture

S3 Bucket → Lambda Function → CloudWatch Logs

(Optional)
EventBridge Schedule → Lambda → S3 Bucket

---

## IAM Permissions

The Lambda execution role was configured with least-privilege permissions.

Permissions used:

- s3:ListBucket
- s3:DeleteObject
- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents

---

## Implementation Steps

1. Created an S3 bucket.
2. Uploaded sample files.
3. Created a Lambda IAM Role.
4. Added an inline IAM policy.
5. Created a Lambda function using Python 3.12.
6. Used a paginator to list all S3 objects.
7. Compared LastModified with the current UTC time.
8. Deleted objects older than the configured threshold.
9. Logged deleted object names to CloudWatch.
10. Tested the Lambda function manually.

---

## Testing

The Lambda function was invoked manually.

Expected Result:

- Old files were deleted.
- New files remained in the bucket.
- Deleted object names appeared in CloudWatch Logs.

---

## Output

Successfully deleted objects older than the configured age.

---

## Discussion

Amazon S3 Lifecycle Rules are the preferred managed solution for deleting old objects. Lambda is useful when deletion depends on custom conditions, object naming patterns, metadata, or additional actions such as notifications.

---

## Cleanup

- Deleted test files.
- Deleted test bucket.
- Deleted Lambda function.
- Deleted IAM role.