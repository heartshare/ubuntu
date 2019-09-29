# Step 1. Run 2 nodes nginx revers proxy for minio
0. Fill inventory with correct info (name nodes, ip-nodes)
0. Install keepalived with running command: ansible-playbook -i ubuntu.inventory nginx_vrrp.yml --tags nginxvrrpinstall
0. Configure and run keepalived with running command: ansible-playbook -i ubuntu.inventory nginx_vrrp.yml --tags nginxvrrpconfigure

# Step 2. Install minio
0. Fill inventory with correct info (name nodes, ip-nodes)


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
