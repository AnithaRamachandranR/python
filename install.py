import os
def fun(data):
    #print(data)
    try:
        print(data)
        __import__(data)
        #importlib.import_module(data)
        
       # os.system('import {}'.format(data))
    except ImportError:
        print ("Trying to Install required module: {}\n".format(data))
        print('python -m pip install {}'.format(data))
        os.system('python -m pip install {}'.format(data))
f = open("app.py", "r")
for i in f:
   if "from" in i:
         list_of_words = i.split('from')
         word = list_of_words[1].split('import')
         data=word[0].strip()
         print(data)
         fun(data)
   elif "import" in i:
    word= i.split('import')
    data=word[1].strip()
    print(data)
    fun(data)
