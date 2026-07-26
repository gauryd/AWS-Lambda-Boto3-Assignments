import boto3

s3 = boto3.client("s3")
sns = boto3.client("sns")

TOPIC_ARN = "arn:aws:sns:us-east-1:334687118615:S3AuditTopic"

def lambda_handler(event, context):

    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:

        name = bucket["Name"]

        try:
            policy = s3.get_bucket_policy_status(Bucket=name)

            if policy["PolicyStatus"]["IsPublic"]:

                sns.publish(
                    TopicArn=TOPIC_ARN,
                    Subject="Public Bucket Alert",
                    Message=f"{name} is public"
                )

                print(name,"is public")

        except Exception:
            pass

    return {
        "Status":"Completed"
    }