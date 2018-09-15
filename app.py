from flask import Flask
from flask import request
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/json', methods=["POST"])
def json_example():
    json_dict = request.get_json()
    if json_dict is not None:
        print(request.mimetype, json_dict['good'], file=sys.stderr)
        print(type(json_dict['list']), json_dict['list'], file=sys.stderr)
        return "good"
    else:
        return "bad"

if __name__ == "__main__":
    app.run("127.0.0.1", "5000")
