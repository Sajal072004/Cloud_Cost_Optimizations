# AWS Cost Optimization with Lambda and CloudWatch

This repository contains **AWS Lambda scripts** for automating cloud cost optimization tasks.

## Features
- **Cleanup EBS Snapshots**: Deletes unused snapshots older than 30 days.
- **Stop Idle EC2 Instances**: Shuts down instances with low CPU usage.
- **Delete Unused ELBs**: Removes load balancers with no active targets.
- **Terminate Underutilized RDS Instances**: Stops RDS instances with minimal load.
- **Cleanup Detached EBS Volumes**: Deletes unattached storage volumes.


## Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/aws-cost-optimization.git
