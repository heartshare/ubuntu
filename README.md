# Step 1. Run 2 nodes nginx revers proxy for minio backends
0. Fill inventory with correct info (name nodes, ip-nodes - in section [nginxsrv], ubuntu.inventory)
0. Install nginx with running command: ansible-playbook -i nginx.yml

# Step 1. Run 2 nodes keepalived for HA nginx revers proxy
0. Fill inventory with correct info (name nodes, ip-nodes - in section [nginxsrv], ubuntu.inventory)
0. Install keepalived with running command: ansible-playbook -i ubuntu.inventory nginx_vrrp.yml

# Step 3. Install minio
0. Fill inventory with correct info (name nodes, ip-nodes - in section [ubuntufarm], ubuntu.inventory)
0. Install minio with running command: ansible-playbook -i ubuntu.inventory minio.yml --tags minio

# Or install full stack nginx+keepalived+minio with one playbook
0. Fill inventory with correct info (name nodes, ip-nodes in section [nginxsrv],[ubuntufarm] ubuntu.inventory)
0. Install full stack with running command: ansible-playbook -i ubuntu.inventory minio_full_stack.yml

# Add remote host minio to config trought by nginx-balancer
If you want work from minio by cli by nginx balancer nodes
0. Copy mc to /usr/sbin/
0. Set execute flag to mc
0. Add remote minio host to local config:  mcminio config host add minio http://172.0.5.151:9001 zaq1xsw2cde3 123456789 --api S3v4 

# Play with user & files
### Add new host to config
ansible -i ubuntu.inventory ubuntu1 -m shell -a 'mc config host add tenant2 http://172.0.5.101:9002 zaq1xsw2cde3 123456789 --api S3v4'
ubuntu1 | CHANGED | rc=0 >>
Added `tenant2` successfully.

### Create new bucket in tenant2
ansible -i ubuntu.inventory ubuntu1 -m shell -a 'mc mb tenant2/forpic'
ubuntu1 | CHANGED | rc=0 >>
Bucket created successfully `tenant2/forpic`.

### Upload new file into created bucket
ansible -i ubuntu.inventory ubuntu1 -m shell -a 'mc cp /tmp/intest.jpg tenant2/forpic'
ubuntu1 | CHANGED | rc=0 >>
/tmp/intest.jpg:  22.22 KiB / 22.22 KiB  100.00% 662.32 KiB/s 0s

### Create user named "user1" with pass "user1user1"
ansible -i ubuntu.inventory ubuntu1 -m shell -a 'mc admin user add tenant2 user1 user1user1'
ubuntu1 | CHANGED | rc=0 >>
Added user `user1` successfully.

### Add policy for tenant2
ansible -i ubuntu.inventory ubuntu1 -m shell -a 'mc admin policy add tenant2 readAndWrite /tmp/policy.json'
ubuntu1 | CHANGED | rc=0 >>
Added policy `readAndWrite` successfully.

/tmp/policy.json
root@ubuntu1:/tmp# cat /tmp/policy.json
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Effect": "Allow",
     "Action": [
       "s3:*",
   "s3:ListAllMyBuckets"
     ],
     "Resource": [
       "arn:aws:s3:::*"
     ]
   }
 ]
}

### Set policy to user for tenant2
ansible -i ubuntu.inventory ubuntu1 -m shell -a 'mc admin policy set tenant2 readAndWrite user=user1'
ubuntu1 | CHANGED | rc=0 >>
Policy readAndWrite is set on user `user1`

### Attach policy readAndWrite to user1
ansible -i ubuntu.inventory ubuntu1 -m shell -a 'mc admin policy set tenant2 readAndWrite user=user1'
Policy readAndWrite is set on user `user1`

### Add user1 to config
ansible -i ubuntu.inventory ubuntu1 -m shell -a 'mc config host add tenant2user http://172.0.5.101:9002 user1 user1user1 --api s3v4'

### Get file from bucket forpic
0. Login into ubuntu1
0. Upload python script
0. Make thet script executable: chmod +x get_file.py
0. Run python script: ./get_file.py (Enter)
root@ubuntu1:~# ./get_file.py
root@ubuntu1:~# ls -l
total 96
-rwxr-xr-x 1 root root   526 Oct  1 06:20 get_file.py
0. Try open new file: outtest.jpg
