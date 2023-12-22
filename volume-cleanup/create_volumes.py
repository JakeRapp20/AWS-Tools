import boto3
import json

# Run this command first, will implement later. Probably boto3... I'm trying to minimlize packages needed to run. 
# aws ec2 describe-volumes --query 'Volumes[?State==`available`].[VolumeId, Size, State, Iops]'  --output text | sed 's/\t/,/g' > volume.out

session = boto3.Session(profile_name='default')


ec2 = boto3.client ('ec2')

def create_volumes(size):

    response = ec2.create_volume(

        AvailabilityZone='us-east-1a',
        Encrypted=False,
        Size=size,
        VolumeType='gp2',
        DryRun=False

)
    return(response)

for _ in range(5):
    response = create_volumes(10)
    print(response['VolumeId'], ": created!")