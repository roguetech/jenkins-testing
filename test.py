import boto3, sys, json

ec2 = boto3.client('ec2')
responce = ec2.describe_instance_attribute(Attribute='instanceType',
    InstanceId='i-0fffb2393ff39a7ea')

print(response)

print("test python")
