import boto3
from datetime import datetime

ec2 = boto3.client("ec2")

def lambda_handler(event, context):

    instance_id = event["detail"]["instance-id"]

    launch_date = datetime.utcnow().strftime("%Y-%m-%d")

    ec2.create_tags(
        Resources=[instance_id],
        Tags=[
            {
                "Key":"LaunchDate",
                "Value":launch_date
            },
            {
                "Key":"Environment",
                "Value":"Development"
            }
        ]
    )

    print("Tagged:",instance_id)

    return {
        "Instance":instance_id
    }