# MikroTik_Backup_Netmiko
Netmiko backups of MikroTik devices

Also includes a custom module for plugging into ansible to run mikrotik backups.

This is a work in progress. Currently not completely functional.

The stand-alone backup.py script should work. 

# Ansible Module
Sample task:
```
- name: Backup RouterOS
  mtk_backup:
    dest: <path_to_save_config>
    username: <username>
    password: <password>
```