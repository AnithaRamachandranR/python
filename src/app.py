from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def index():
    a=[]
    myfile=open('sample.json','r')
    readfile=myfile.read()
    obj=json.loads(readfile)
    print(obj)
    for data in obj['channels']:
	a.append(data['name'])
    return a


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

