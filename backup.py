#!/usr/bin/python

#import required modules
from netmiko import ConnectHandler
from getpass import getpass
import re

#ip_addrs_file = open('ips.txt')
#devices = ip_addrs_file.read().splitlines()
key_file = open('key.txt')
key_path = key_file.read().splitlines()
devices = ['192.168.3.20']

for ip in devices:
    device = {
        'device_type': 'mikrotik_routeros',
        'ip': ip,
        'port': 22,
        'username': 'ansible',
        #'password': getpass(),
        #'password': 'ansible'
        'use_keys': True,
        'key_file': key_path,
        'verbose': True
    }
    net_connect = ConnectHandler(**device)
    net_connect.enable()

net_connect = ConnectHandler(**device)
net_connect.enable()
#print(net_connect.find_prompt())

#export the device configuration to output variable
output = net_connect.send_command_timing("export")
print(output)

# write output to text file
config = open("config.txt","w")
config.write(output)
config.close()
