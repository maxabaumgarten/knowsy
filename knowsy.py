#This is a very much work in progress.
import platform
import ipaddress
import csv
from address import IpAddress
from operating_system import OperatingSystem

print("Welcome to Knowsy!  I know everything about IP addresses and Domains(coming soon).")

#Determine Operating System information
#This may be removed as program is being developed as OS agnostic
print(f"\nLet's check what operating system you are running.")

os_check =  platform.system()
current_os = OperatingSystem(os_check)
current_os.set_os()
current_os.return_os()

#NOTE: print statements and hardcoded IPs for testing
#TODO for host in host_list.csv, run checks, add to csv

#Test Vars for CSV
testip = "9.9.9.9"
testdomain = "quad9.com"
testping = 'Yes'
testroute = '10.0.1.1 > 6.7.8.9 > 9.9.9.1'

#Create and Setup the CSV
name_request = input("Save Knowsy CSV file as? ")
filename = name_request + '.csv'

with open(filename, 'w') as file_object:
    file_writer = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['IP', 'Domain', 'Ping', 'Routes'])

#Ask user for whole file
hostfile = input("What is the name of your host file (.txt ONLY)? ")


with open(hostfile, "r") as h_file:
    for host in h_file:
        #Validate IP
        ip = IpAddress(host.rstrip())
        if ip.validate_ip():
            #Ping Test
            ping_answer = ip.ping_check(current_os.return_os())
            with open(filename, 'a') as file_object:
                file_writer = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                file_writer.writerow([ip.return_ip_address(), testdomain, ping_answer, testroute])
        else:
            print(f"{ip.return_ip_address()} is not valid.")0