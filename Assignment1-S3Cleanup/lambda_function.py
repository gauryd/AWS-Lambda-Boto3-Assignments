import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = 's3-bucket-cleanup-demo-12345'

AGE = timedelta(minutes=2)

def lambda_handler(event, context):

    now = datetime.now(timezone.utc)

    paginator = s3.get_paginator('list_objects_v2')

    deleted = []

    for page in paginator.paginate(Bucket=BUCKET_NAME):

        if 'Contents' not in page:
            continue

        for obj in page['Contents']:

            if now - obj['LastModified'] > AGE:

                s3.delete_object(
                    Bucket=BUCKET_NAME,
                    Key=obj['Key']
                )

                print(f"Deleted: {obj['Key']}")
                deleted.append(obj['Key'])

    return {
        "Deleted Objects": deleted
    }