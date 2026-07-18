from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "timestamp": datetime.utcnow().isoformat()}), 200

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the DevOps demo API"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)