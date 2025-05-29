from flask import Flask, jsonify
from os import environ
from threading import Thread

crowthon = Flask(__name__)

@crowthon.route("/favicon.ico")
def favicon():
    return "", 204

@crowthon.route("/")
def index():
    status = {
        "name": "Crowthon",
        "type": "Userbot",
        "status": "Alive"
    }
    return jsonify(status)

def run_server():
    port = int(environ.get("PORT", 8080))
    crowthon.run(host="0.0.0.0", port=port)

def keep_alive():
    thread = Thread(target=run_server)
    thread.start()
