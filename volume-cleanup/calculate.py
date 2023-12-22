import boto3

# Initializes boto3 ec2 for later use below
ec2 = boto3.client ('ec2')



def filter_available_volumes():
    response = ec2.describe_volumes(Filters=[{'Name': 'status','Values': ['available']}])
    volume_ids = [volume['VolumeId'] for volume in response['Volumes']]
    return volume_ids


def calculate_gb_used(volume_id):
    response = ec2.describe_volumes(VolumeIds=volume_id)
    total_gbs = sum([ i['Size'] for i in response['Volumes']])
    return total_gbs



def calculate_iops_used(volume_id, free_iops):
    response = ec2.describe_volumes(VolumeIds=volume_id)
    total_gp3_iops = sum([i['Iops'] - free_iops for i in response['Volumes'] if i['Iops'] > free_iops])
    return total_gp3_iops


# total_gbs = (calculate_gb_used(available_volume_ids))

# # Prints total amount of volumes
# print("Total unused EBS volumes: " + str(len(available_volume_ids)))


# total_iops = calculate_iops_used(available_volume_ids, 50)


# total_savings_per_year = (total_gbs * .9) + (total_iops * .005) * 12

# print(total_savings_per_year)
