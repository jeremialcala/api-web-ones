import logging
import json
from flask import Flask, Response, request

app = Flask(__name__)


@app.route(rule="/", methods=["GET"])
def get_home():
    return Response(json.dumps({"msg": "Process OK"}), status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True, port=3005)
