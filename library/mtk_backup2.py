import json
from ansible.module_utils._text import to_text
from ansible.module_utils.basic import env_fallback
from ansible.module_utils.network.common.utils import to_list, ComplexList
from ansible.module_utils.connection import Connection, ConnectionError
import re
from netmiko import ConnectHandler

_DEVICE_CONFIGS = {}

def main():
    module = routeros_provider_spec = {
            'host': dict(),
            'port': dict(type='int'),
            'username': dict(fallback=(env_fallback, ['ANSIBLE_NET_USERNAME'])),
            'password': dict(fallback=(env_fallback, ['ANSIBLE_NET_PASSWORD']), no_log=True),
            'ssh_keyfile': dict(fallback=(env_fallback, ['ANSIBLE_NET_SSH_KEYFILE']), type='path'),
            'timeout': dict(type='int'),
            'destination': dict(type='path', default='config.txt', aliases=['dest', 'name', 'path'])
        }
    routeros_argument_spec = {}

    path = module.params.get('path')
    host = module.params.get('host')
    port = module.params.get('port')
    password = module.params.get('password')
    username = module.params.get('username') 
    
    device = {
        'device_type': 'mikrotik_routeros',
        'ip': host,
        'port': port,
        'username': username,
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

    #return is_error, has_changed, meta

    #is_error, has_changed, result = mtk_backup_config(module.params)

    # if not is_error:
    #     module.exit_json(changed=has_changed, meta=result)
    # else:
    #     module.fail_json(msg="Error backing up RouterOS", meta=result)

if __name__ == '__main__':
    main()


