import boto3
import pprint

# Importing credentials from aws_credentials.conf file in local directory
# Cleaned New line from file reading
creds = open("C:\\Users\\Jacob\\Desktop\\aws_credentials.conf", 'r')
aws_access_key_id = creds.readline()
clean_access_key = aws_access_key_id.replace('\n', '')
aws_secret_access_key = creds.readline()
clean_secret_key = aws_secret_access_key.replace('\n', '')
region_name = creds.readline()
creds.close()

# Created session for all API calls to AWS
session = boto3.Session(clean_access_key, clean_secret_key, region_name = region_name)

ec2_client = session.client('ec2')
response = ec2_client.describe_instances()
 
#Loops through ec2-describe for status of Instance Name, ID, and State
for i in response['Reservations']:
    state = i['Instances'][0]['State']['Name']
    instance_id = i['Instances'][0]['InstanceId']
    tag = i['Instances'][0]['Tags']
    for x in tag:
        if x['Key'] == "Name":
            name = x['Value']
    print("{:<20} {:<15} {:<10}".format(name, instance_id, state))



