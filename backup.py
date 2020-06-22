from netmiko import ConnectHandler
from getpass import getpass
import re

ip_addrs_file = open('ips.txt')
devices = ip_addrs_file.read().splitlines()

for ip in devices:
    device = {
        'device_type': 'mikrotik_routeros',
        'ip': ip,
        'username': 'ansible',
        #'password': getpass(),
        #'password': 'ansible'
        'key_filename': ''
    }
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    #print(net_connect.find_prompt())

net_connect = ConnectHandler(**device)