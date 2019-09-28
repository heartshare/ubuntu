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
