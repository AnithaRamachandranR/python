
from flask import Flask

app = Flask(__name__)

@app.route("/ani")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()
