
# AWS Cost Optimization with Lambda and CloudWatch

This repository contains **AWS Lambda scripts** for automating cloud cost optimization tasks.  
By leveraging **CloudWatch** and **Lambda**, these scripts help detect and mitigate unnecessary cloud expenses.

## 🚀 Features
- **Cleanup EBS Snapshots**: Deletes unused snapshots older than 30 days.
- **Stop Idle EC2 Instances**: Shuts down instances with low CPU usage.
- **Delete Unused ELBs**: Removes load balancers with no active targets.
- **Terminate Underutilized RDS Instances**: Stops RDS instances with minimal load.
- **Cleanup Detached EBS Volumes**: Deletes unattached storage volumes.

## 🛠️ Setup

### 1️⃣ Clone the repository:
```sh
git clone https://github.com/Sajal072004/Cloud_Cost_Optimizations.git
cd Cloud_Cost_Optimizations
```

### 2️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```

### 3️⃣ Deploy Lambda functions:
- Navigate to the **AWS Lambda Console**.
- Create a new function and **upload the corresponding script**.
- Assign appropriate IAM permissions.
- Set up a **CloudWatch trigger** to execute the function periodically.

## 📂 Repository Structure
```
Cloud_Cost_Optimizations/
│── lambda-scripts/
│   ├── cleanup_ebs_snapshots.py
│   ├── stop_idle_ec2.py
│   ├── delete_unused_elbs.py
│   ├── terminate_underutilized_rds.py
│   ├── cleanup_detached_ebs.py
│── requirements.txt
│── README.md
```

