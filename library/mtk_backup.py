#!/usr/bin/python

from ansible.module_utils.basic import *
from netmiko import ConnectHandler
from getpass import getpass
import re

def mtk_backup_config(data):
    is_error = False
    has_changed = False

    device = {
        'device_type': 'mikrotik_routeros',
        'ip': host,
        'port': port,
        'username': username,
        #'password': getpass(),
        'password': password,
        #'use_keys': True,
        #'key_file': key_path,
        #'verbose': True
    }


    flag = "Backup"

    net_connect = ConnectHandler(**device)
    net_connect.enable()

    net_connect = ConnectHandler(**device)
    net_connect.enable()
    #print(net_connect.find_prompt())

    #export the device configuration to output variable
    output = net_connect.send_command_timing("export")
    #print(output)

    # write output to text file
    config = open(path,"w")
    config.write(output)
    config.close()

    has_changed = True

    resp = {
        "config": output,
        "result": flag,
    }

    meta = {"status" : "OK", "response" : resp}

    return is_error, has_changed, meta

def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True, aliases=['dest', 'name']),
            host=dict(type='str', required=True, default='localhost', aliases=['ip','hostname']),
            port=dict(type='int', required = False, default=22),
            username=dict(type='str', required = True, aliases=['user']),
            password=dict(type='str', required = True),
        ),
        supports_check_mode=False,
    )

    path = module.params.get('path')
    host = module.params.get('host')
    port = module.params.get('port')
    password = module.params.get('password')
    username = module.params.get('username')

    is_error, has_changed, result = mtk_backup_config(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error backing up RouterOS", meta=result)

if __name__ == '__main__':
    main()