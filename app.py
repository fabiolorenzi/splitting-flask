from flask import Flask

from model import Articles

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/test", methods=["GET"])
def test():
    return "Hello world"

@app.route("/class", methods=["GET"])
def classer():
    d = Articles("hello", "yeah")
    print(d.body)
    return "helo"

import route

if __name__ == "__main__":
    app.run(debug=True)