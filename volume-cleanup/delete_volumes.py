import boto3 

ec2 = boto3.client ('ec2')

# deletes volume based on volume_id
def delete_available_volumes(volume_id):
    ec2.delete_volume(VolumeId=volume_id)
    print(volume_id + " deleted!")