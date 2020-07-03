
from flask import Flask
import subprocess
import sys
app = Flask(__name__)
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
print(installed_package)
@app.route("/ani")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()
