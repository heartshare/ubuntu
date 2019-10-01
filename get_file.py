#!/usr/bin/python3

from minio import Minio
from minio.error import ResponseError

minioClient = Minio('172.0.5.101:9002',
                  access_key='zaq1xsw2cde3',
                  secret_key='123456789',
                  secure=False,
                  http_client=None)

try:
    data = minioClient.get_partial_object('forpic','intest.jpg',offset=1000)
    with open('./outtest.jpg', 'wb') as file_data:
        for d in data:
            file_data.write(d)
except ResponseError as err:
    print(err)
