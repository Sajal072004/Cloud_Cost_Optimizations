import boto3
import datetime

rds = boto3.client('rds')
cloudwatch = boto3.client('cloudwatch')

CPU_THRESHOLD = 10  # Percentage
BUSINESS_HOURS = range(9, 18)  # 9 AM - 6 PM

def lambda_handler(event, context):
    current_hour = datetime.datetime.utcnow().hour

    if current_hour in BUSINESS_HOURS:
        return "Skipping RDS shutdown during business hours."

    instances = rds.describe_db_instances()

    for instance in instances['DBInstances']:
        instance_id = instance['DBInstanceIdentifier']

        metrics = cloudwatch.get_metric_statistics(
            Namespace='AWS/RDS',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'DBInstanceIdentifier', 'Value': instance_id}],
            StartTime=(datetime.datetime.utcnow() - datetime.timedelta(minutes=30)).isoformat(),
            EndTime=datetime.datetime.utcnow().isoformat(),
            Period=300,
            Statistics=['Average']
        )

        if metrics['Datapoints'] and metrics['Datapoints'][0]['Average'] < CPU_THRESHOLD:
            rds.stop_db_instance(DBInstanceIdentifier=instance_id)
            print(f"Stopped underutilized RDS instance: {instance_id}")

    return "Underutilized RDS instances stopped."
