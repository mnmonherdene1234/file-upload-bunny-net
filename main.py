from flask import Flask, request, jsonify
from ftplib import FTP

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify(message="Hello World")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    ftp = FTP("sg.storage.bunnycdn.com", "script-slayer-zone",
              "80766680-ea9e-4841-be2de97f101f-935b-4f96")
    ftp.storbinary(f"STOR /trash/{file.filename}", file.stream)
    ftp.quit()

    return jsonify(url=f"https://script-slayer.b-cdn.net/trash/{file.filename}")
