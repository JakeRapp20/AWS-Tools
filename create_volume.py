import boto3
import json

# Run this command first, will implement later. Probably boto3... I'm trying to minimlize packages needed to run. 
# aws ec2 describe-volumes --query 'Volumes[?State==`available`].[VolumeId, Size, State, Iops]'  --output text | sed 's/\t/,/g' > volume.out

session = boto3.Session(profile_name='default')


ec2 = boto3.client ('ec2')

# def create_volumes(size):

#     response = ec2.create_volume(

#         AvailabilityZone='us-east-1a',
#         Encrypted=False,
#         Size=size,
#         VolumeType='gp2',
#         DryRun=False

# )

# create_volumes(15)

# def delete_volume(volume_id):

#     response = ec2.delete_volume(
#         VolumeId=volume_id
#     )

# delete_volume("vol-0a05833c8c20d4162")


def list_volumes():

    response = ec2.describe_volumes()
    print(type(response))

    input = json.loads(response)
    output = json.dumps(input)
    print(output)
list_volumes()