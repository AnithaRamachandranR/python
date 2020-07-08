import boto3
import os
from os import listdir
from os.path import isfile, join
ACCESS_KEY = ''
SECRET_KEY = ''
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
mypath="/home/ec2-user/anitha/"
buck_obj=[]
filename=[]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
    if i.endswith(".txt"):
        filename.append(i)
data=s3.list_objects_v2(Bucket='anitha-bucket')
for i in data['Contents']:
    buck_obj.append(i['Key'])
#li_u_removed = [i.encode('utf-8') for i in buck_obj]
#print("bucket",buck_obj)
#print(li_u_removed)
#print(filename,buck_obj)
"""data=set(filename)-set(buck_obj)
list_data=list(data)
if len(list_data)>0:
    return 1
else :
    return 0"""
#print(filename,buck_obj)
try:
    for files in filename:
        if files not in buck_obj:
            raise "Error"
    print("0")
except :
    print("1")
#    return 0
