import boto3
from delete_volumes import delete_available_volumes
from calculate import calculate_gb_used, calculate_iops_used, filter_available_volumes


# Builds session with access keys is AWS CONFIGURE
session = boto3.Session(profile_name='default')

# Initializes boto3 ec2 for later use below
ec2 = boto3.client ('ec2')

# Retreives availiable Volumes
available_volume_ids = filter_available_volumes()




def show_menu():
    print("Main Menu:")
    print("1. Calcluate EBS Cost Savings")
    print("2. List EBS Volumes to be Deleted")
    print("3. Delete Unused EBS Volumes")
    print("4. Quit")

def option1():
    print("Calculating EBS Cost Savings")
    available_volume_ids = filter_available_volumes()
    total_unused_volumes = len(available_volume_ids)
    total_gbs = (calculate_gb_used(available_volume_ids))
    total_iops = calculate_iops_used(available_volume_ids, 50)

    total_savings_per_year = (total_gbs * .9) + (total_iops * .005) * 12

    print("Total unused volumes: " + str("{:,}".format(total_unused_volumes)))
    print("Total unused EBS GBs: " + str(len(available_volume_ids)) + " GBs")
    print("Total unused EBS IOPS: " + str("{:,}".format(total_iops)))
    print("Total savings per year: $"+ (str("{:,.2f}".format(total_savings_per_year))))
    


def option2():
    print("Listing EBS Volumes to be Deleted")
    available_volume_ids = filter_available_volumes()
    for volumes in available_volume_ids:
        print(volumes, "will be deleted!")

def option3():
    print(" Deleting Unsused EBS Volumes")
    available_volume_ids = filter_available_volumes()
    for volumes in available_volume_ids:
        delete_available_volumes(volumes)

# Main loop
while True:
    # Display the menu
    show_menu()

    # Get user input
    choice = input("Enter your choice (1-4): ")

    # Process the user's choice
    if choice == '1':
        option1()
    elif choice == '2':
        option2()
    elif choice == '3':
        option3()
    elif choice == '4':
        break
    else:
        print("Invalid option")

    # Wait for user input before going back to the main menu
    input("Press Enter to return to main menu...")








