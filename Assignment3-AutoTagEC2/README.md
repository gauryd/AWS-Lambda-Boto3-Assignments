# Assignment 3 - Auto Tag EC2 Instances on Launch

## Objective

Automatically tag EC2 instances when they enter the Running state using Amazon EventBridge and AWS Lambda.

---

## AWS Services Used

- Amazon EC2
- AWS Lambda
- Amazon EventBridge
- IAM
- Amazon CloudWatch
- Python 3.12
- Boto3

---

## Architecture

EC2 Instance Running

↓

Amazon EventBridge

↓

AWS Lambda

↓

EC2 CreateTags API

↓

CloudWatch Logs

---

## IAM Permissions

The Lambda execution role was configured with least-privilege permissions.

Permissions used:

- ec2:CreateTags
- ec2:DescribeInstances
- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents

---

## Implementation Steps

1. Created a Lambda IAM Role.
2. Added an inline IAM policy.
3. Created a Lambda function using Python 3.12.
4. Configured an EventBridge rule for EC2 Instance State-change Notification.
5. Configured the event to trigger only when the instance state became Running.
6. Lambda extracted the Instance ID from the EventBridge event.
7. Added LaunchDate and Environment tags to the EC2 instance.
8. Verified the tags in the EC2 console.

---

## Testing

Launched a new EC2 instance.

Expected Result:

- Lambda executed automatically.
- LaunchDate tag added.
- Environment tag added.
- CloudWatch Logs showed successful execution.

---

## Output

EC2 instances were automatically tagged after launch.

---

## Discussion

EventBridge enables automatic event-driven automation without manual intervention. This approach is useful for enforcing organizational tagging standards for resource tracking and cost allocation.

---

## Cleanup

- Deleted EventBridge rule.
- Deleted Lambda function.
- Deleted IAM role.
- Terminated test EC2 instance.