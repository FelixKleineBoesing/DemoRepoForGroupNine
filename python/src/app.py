from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST", "GET"])
def process():
    return "This is the root page"


@app.route("/name", methods=["POST", "GET"])
def input_name():
    if "my-name" in request.args:
        return request.args.get("my-name")
    return "Name!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)