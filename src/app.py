from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(host='54.81.27.240', port=5000)

