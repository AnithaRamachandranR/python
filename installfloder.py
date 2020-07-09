from os import listdir
from os.path import isfile, join
import os
def fun(data):
    try:
            __import__(data)
    except ImportError:
        print ("Trying to Install required module: {}\n".format(data))
        os.system('python -m pip install {}'.format(data))
mypath="/home/ec2-user/python_file/"
for k in listdir(mypath):
            print(k)
            with open(mypath +k,'r') as a:
                 print(a)
                 for i in a:
                      if i.startswith('from'):
                          list_of_words =((i.split('from'))[1].split('import'))[0].strip()
                          print(list_of_words)
                          fun(list_of_words)
                      elif i.startswith('import'):
                          word=(i.split('import'))[1].strip()
                          print(word)
                          fun(word)

""" #   if isfile(join(mypath,k)):
  #      for j in k:
            with open(k) as f:
                for i in f:
                    if i.startswith('from'):
                        list_of_words =((i.split('from'))[1].split('import'))[0].strip()
                        print(list_of_words)
                        fun(list_of_words)
                    elif i.startswith('import'):
                        word=(i.split('import'))[1].strip()
            #word=i.split('import')
            #data=word[1].strip()
                        print(word)
                        fun(word)
    #data=list_of_words[]

        # print(list_of_words[1])
   #list_of_words = i.split('import')
   #data=list_of_words[-1].strip()
                                                                               
