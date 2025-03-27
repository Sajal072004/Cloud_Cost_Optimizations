import boto3

cloudwatch = boto3.client('cloudwatch')
ec2 = boto3.client('ec2')

CPU_THRESHOLD = 5  # Percentage
IDLE_DURATION = 1800  # 30 minutes in seconds

def lambda_handler(event, context):
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']

            metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=(datetime.datetime.utcnow() - datetime.timedelta(minutes=30)).isoformat(),
                EndTime=datetime.datetime.utcnow().isoformat(),
                Period=300,
                Statistics=['Average']
            )

            if metrics['Datapoints'] and metrics['Datapoints'][0]['Average'] < CPU_THRESHOLD:
                ec2.stop_instances(InstanceIds=[instance_id])
                print(f"Stopped idle instance: {instance_id}")

    return "Idle EC2 instances stopped."
