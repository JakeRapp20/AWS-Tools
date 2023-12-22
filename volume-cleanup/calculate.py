
import csv
import boto3

# Run this command first, will implement later. Probably boto3... I'm trying to minimlize packages needed to run. 
# aws ec2 describe-volumes --query 'Volumes[?State==`available`].[VolumeId, Size, State, Iops]'  --output text | sed 's/\t/,/g' > volume.out

session = boto3.Session(profile_name='default')




total_gb = 0
with open('volume.out') as f:
    read = csv.reader(f)
    for row in read:
        total_gb += int(row[1])
f.close()

total_gb_saved = float(total_gb) * .10 * 12

total_iops_difference = 0
with open('volume.out') as f:
    read = csv.reader(f)
    for row in read:
        if int(row[3]) > 3000:
            difference = int(row[3]) - 3000 
            total_iops_difference += difference
f.close()

total_iops_savings = .005 * total_iops_difference * 12

grand_total_saved = total_iops_savings + total_gb_saved

print ("Total GBs unused: " + "{:,}".format(total_gb))

print("Total IOPS unused: " + "{:,}".format(total_iops_difference))

print ("Total saved in EBS costs per year: $" + "{:,.2f}".format(total_gb_saved))

print("Total saved in IOPS costs per year: $" + "{:,.2f}".format(total_iops_savings))

print("Grand total saved per year: $" "{:,.2f}".format(grand_total_saved))


