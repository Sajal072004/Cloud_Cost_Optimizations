import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])

    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        ec2.delete_volume(VolumeId=volume_id)
        print(f"Deleted detached EBS volume: {volume_id}")

    return "Unused EBS volumes cleaned up."
