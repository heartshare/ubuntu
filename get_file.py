#!/bin/python

from minio import Minio
from minio.error import ResponseError

pic_name = ''
pic_size = 0

minioClient = Minio('172.0.5.151:9002',
                  access_key='zaq1xsw2cde3',
                  secret_key='123456789',
                  secure=False,
				  http_client=None)

objects = minioClient.list_objects('forpic', prefix=None,recursive=True)

for obj in objects:
	pic_name = obj.object_name.encode('utf-8')
	pic_size = obj.size

print(pic_name, pic_size)


# Get a full object and prints the original object stat information.
#try:
#    print(minioClient.fget_object('forpic', pic_name, '/tmp/myobject'))
#except ResponseError as err:
#    print(err)

try:
    data = minioClient.get_partial_object('forpic',pic_name,offset=1000,length=pic_size)
    with open('./test.jpg', 'wb') as file_data:
        for d in data:
            file_data.write(d)
except ResponseError as err:
    print(err)
