import boto3

elbv2 = boto3.client('elbv2')

def lambda_handler(event, context):
    elbs = elbv2.describe_load_balancers()

    for elb in elbs['LoadBalancers']:
        elb_arn = elb['LoadBalancerArn']
        target_groups = elbv2.describe_target_groups(LoadBalancerArn=elb_arn)['TargetGroups']

        is_unused = all(not tg['TargetHealthDescriptions'] for tg in target_groups)

        if is_unused:
            elbv2.delete_load_balancer(LoadBalancerArn=elb_arn)
            print(f"Deleted unused ELB: {elb_arn}")

    return "Unused ELBs cleaned up."
