import boto3

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

for _ in range(20):
    response = create_volumes(10)
    print(response['VolumeId'], ": created!")