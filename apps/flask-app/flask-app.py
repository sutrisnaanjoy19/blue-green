from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def say_hello():
    return "<p>ARGOCD testing flask app vesion **2**</p>"


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", debug=True)