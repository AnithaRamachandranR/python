from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def index():
    myfile=open('sample.json','r')
    readfile=myfile.read()
    obj=json.loads(readfile)
    print(obj)
    return "Hello, world!"+obj


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

