
from flask import Flask
import boto3
app = Flask(__name__)
@app.route("/ani")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
