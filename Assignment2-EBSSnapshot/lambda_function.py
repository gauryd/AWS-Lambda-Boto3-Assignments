import boto3
from datetime import datetime, timezone, timedelta

ec2 = boto3.client("ec2")

VOLUME_ID = "vol-0c51372264f3eb512"

RETENTION = timedelta(days=30)

def lambda_handler(event, context):

    snapshot = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description="Lambda Backup"
    )

    snapshot_id = snapshot["SnapshotId"]

    ec2.create_tags(
        Resources=[snapshot_id],
        Tags=[
            {"Key": "CreatedBy", "Value": "Lambda-Backup"}
        ]
    )

    print("Created Snapshot:", snapshot_id)

    snapshots = ec2.describe_snapshots(
        OwnerIds=["self"],
        Filters=[
            {
                "Name": "tag:CreatedBy",
                "Values": ["Lambda-Backup"]
            }
        ]
    )

    now = datetime.now(timezone.utc)

    for snap in snapshots["Snapshots"]:

        if now - snap["StartTime"] > RETENTION:

            ec2.delete_snapshot(
                SnapshotId=snap["SnapshotId"]
            )

            print("Deleted:", snap["SnapshotId"])

    return {
        "Snapshot": snapshot_id
    }