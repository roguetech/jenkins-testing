import boto3, sys, json

ec2 = boto3.client('ec2', region_name='eu-west-1')
responce = ec2.describe_instance_status()

print(response)

print("test python")
