from netmiko import ConnectHandler
from getpass import getpass
import re

#ip_addrs_file = open('ips.txt')
#devices = ip_addrs_file.read().splitlines()
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
        'key_file': "~\\.ssh\\ansible_rsa"
    }
    net_connect = ConnectHandler(**device)
    net_connect.enable()

net_connect = ConnectHandler(**device)
net_connect.enable()
print(net_connect.find_prompt())