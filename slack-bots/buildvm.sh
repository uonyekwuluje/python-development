#!/bin/bash
VM=$1
PROXMOX_HOST="192.168.1.146"
#sshpass -p 'liloslilos' ssh root@$PROXMOX_HOST pvesh get /cluster/nextid
cp vm-template.sh vm.sh
sed -i "s/PROXMOX_GUEST/$VM/g" vm.sh
chmod a+x vm.sh
sshpass -p 'liloslilos' scp vm.sh root@$PROXMOX_HOST:/tmp
sshpass -p 'liloslilos' ssh root@$PROXMOX_HOST /tmp/vm.sh
