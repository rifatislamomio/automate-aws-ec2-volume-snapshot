import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Maximum number of snapshots of a volume
MAX_SNAPSHOTS = int(os.environ["MAX_SNAPSHOTS"])
# Volume id of EC2 instance
VOLUME_ID = os.environ["VOLUME_ID"]

client = boto3.client("ec2")
response = client.create_snapshot(
    Description="Root volume snapshot: " + VOLUME_ID, VolumeId=VOLUME_ID
)
print("New snapshot: ", response["SnapshotId"])

descSnapshots = client.describe_snapshots(
    Filters=[{"Name": "volume-id", "Values": [VOLUME_ID]}]
)

snapshots = []
if len(descSnapshots["Snapshots"]):
    snapshots = sorted(
        descSnapshots["Snapshots"], key=lambda x: x["StartTime"], reverse=True
    )

print("Available snapshots:")
for snapshot in snapshots:
    print(f"{snapshot["SnapshotId"]} ({snapshot["State"]})")
print()

if len(snapshots) > MAX_SNAPSHOTS:
    removeableSnapshots = snapshots[MAX_SNAPSHOTS:]
    for snapshot in removeableSnapshots:
        response = client.delete_snapshot(
            SnapshotId=snapshot["SnapshotId"], DryRun=False
        )
        print("Deleted snapshot: ", snapshot["SnapshotId"])
