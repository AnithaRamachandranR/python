import os
def fun(data):
    try:
            __import__(data)
    except ImportError:
        print ("Trying to Install required module: {}\n".format(data))
        os.system('python -m pip install {}'.format(data))
f = open("/home/ec2-user/app.py", "r")
for i in f:
        if "from" in i and not i.startswith('#'):
            list_of_words =((i.split('from'))[1].split('import'))[0].strip()
            print(list_of_words)
            fun(list_of_words)
        elif "import" in i and not i.startswith('#'):
            word=(i.split('import'))[1].strip()
            print(word)
            fun(word)
