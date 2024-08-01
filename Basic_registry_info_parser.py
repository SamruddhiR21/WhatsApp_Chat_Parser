#Paths of file parsed with regripper
path_system=input(r"Enter path of SYSTEM file parsed with regripper:")
path_software=input(r"Enter path of SOFTWARE file parsed with regripper:")
path_SAM=input(r"Enter path of SAM file parsed with regripper:")

#Command for writing output to file
import os

# file and directory listing



#print(path1)
f1 = open(path_system, "r", encoding="utf-16")
lines = f1.readlines()
print("*"*15, "Basic Information", "*"*15)
print("="*50)
for line in lines:
    if "TCP/IP Hostname" in line:
        print(line)
        print("="*50)
    if "DhcpIPAddress" in line:
        print(line)
        print("="*50)
    if "ShutdownTime =" in line:
        print(line)
        print("="*50)
  
#to get 7 lines after the keyword        
for i, line in enumerate(lines):
    if "ControlSet001\Control\TimeZoneInformation" in line:
        #a=lines[max(i - 5, 0) : i + ]
        a=lines[max (i,0): i + 7]
        n = 1
        for lines in a:
            print(lines)
            n += 1
        print("="*50)
        
f1 = open(path_software, "r", encoding="utf-16")
lines = f1.readlines()
for line in lines:
    if "ProductName =" in line:
       print(line)
    if "InstallDate =" in line:
       print(line)
       print("="*50)
for line in lines:
    if "LastLoggedOnUser" in line:
       print(line)
print("="*50)

print("Domain Accounts")
for line in lines:
    if "Path      :" in line:
        print(line)
    if "SID       :" in line:
       print(line)
print("="*50)        
      
f1 = open(path_SAM, "r", encoding="utf-16")
lines = f1.readlines()
print("User Information - Usernames")
for line in lines:
    if "Username" in line:
       print(line)
print("="*50)


print("App path:-Installed/Unistalled Apps")
f1 = open(path_software, "r",  encoding="utf-16")
for line in iter(f1.readline, 'Microsoft\\Windows\\CurrentVersion\\App Paths\n'):
    pass
for line in iter(f1.readline,'Wow6432Node\n'):
    if "REG" in line: #Replace REG with - to see all enteries
        print(line)

print("="*50)
print("Drive Letter & Volume Names")
f1 = open(path_software, "r",  encoding="utf-16")
for line in iter(f1.readline, 'Microsoft\\Windows Portable Devices\\Devices\n'):
    pass
for line in iter(f1.readline,'Microsoft\\Windows\\CurrentVersion\\Installer\\UserData\n'):
    if "Device    :" in line:
        print(line)
    if "SN        :" in line:
        print(line)
'''        
print("="*50)
print("USB Devices")
f1 = open(path_system, "r", encoding="utf-16")
for line in iter(f1.readline, 'ControlSet001\\Enum\\USBStor\n'):
    pass
for line in iter(f1.readline, 'usbstor2\n'):
    if "S/N:" in line:
        print(line)
    if "FriendlyName    :" in line:
        print(line)

print("="*50)
'''
os.system("python G:\Python\My\Module\Basic_registry_info_parser.py > output10.txt")

