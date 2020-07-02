from flask import Flask,render_template
import json

app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
    return render_template('front.html')
   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

