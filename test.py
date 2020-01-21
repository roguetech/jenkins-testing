import boto3, sys, json

ec2 = boto3.client('ec2')
response = ec2.describe_instance_status()

print(response)

print("test python")
