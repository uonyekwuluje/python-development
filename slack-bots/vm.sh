#!/bin/bash
export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Get VM ID
vm_id=$(pvesh get /cluster/nextid)

# Create VM Disk
mkdir -p /mnt/storage2/images/${vm_id}/
qemu-img create -f qcow2 /mnt/storage2/images/${vm_id}/vm-${vm_id}-disk-0.qcow2 40G

# Create VM Shell
qm create ${vm_id} --agent enabled=1 \
--description "testbaby Server" \
--name testbaby --cores 2 --sockets 2 --memory 6048 \
--net0 virtio,bridge=vmbr0 --serial0 socket \
--scsihw virtio-scsi-pci --ostype l26 \
--scsi0 size=40G,file=vm_storage:${vm_id}/vm-${vm_id}-disk-0.qcow2

# Start Guest
qm start ${vm_id}
