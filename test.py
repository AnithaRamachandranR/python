from __future__ import unicode_literals
import boto3
import os
import sys
# coding=utf-8
ACCESS_KEY = 'AKIAJEJD4WFA24VOBHYA'
SECRET_KEY = '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'
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
dir2=[]
dir2= sys.argv[1:]
#print("dir2",dir2)
dir3=[x.decode('ascii') for x in dir2]
#print("dir3",dir3)
dir1=[]
resp = s3.list_objects_v2(Bucket='anitha-bucket')
for obj in resp['Contents']:
    if obj['Size']>0:
            dir1.append((obj['Key'].split("/"))[-1].strip())
#print(dir1)
resdir=set(dir3)-set(dir1)
if len(list(resdir)) != 0:
      print ("1")
else:
      print ("0")
