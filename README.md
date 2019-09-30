# Step 1. Run 2 nodes nginx revers proxy for minio backends
0. Fill inventory with correct info (name nodes, ip-nodes)
0. Install nginx with running command: ansible-playbook -i nginx.yml

# Step 1. Run 2 nodes keepalived for HA nginx revers proxy
0. Fill inventory with correct info (name nodes, ip-nodes)
0. Install keepalived with running command: ansible-playbook -i ubuntu.inventory nginx_vrrp.yml

# Step 3. Install minio
0. Fill inventory with correct info (name nodes, ip-nodes)
0. Install minio with running command: ansible-playbook -i ubuntu.inventory minio.yml --tags minio

# Or install full stack nginx+keepalived+minio with one playbook
0. Fill inventory with correct info (name nodes, ip-nodes)
0. Install full stack with running command: ansible-playbook -i ubuntu.inventory minio_full_stack.yml

# add tenant1 to host
mc config host add tenant1 http://172.0.5.101:9001 zaq1xsw2cde3 123456789

# list bucket in tenant1
mc ls tenant1

# remove tenant2 from host
mc config host rm tenant2

# create bucket in tenant1
mc mb tenant1/clicreate

# upload file 'syslog' into tenant/bucket
mc cp /var/log/syslog tenant1/forpic

# remove file 'syslog' from tenant/bucket
mc rm tenant1/forpic/syslog
