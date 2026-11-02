import os
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY") # reads environment variable
LOG_FILE = "/logs/requests.log" # sets the file location

assets = [
    {"id": "R1", "device_type": "router", "ip": "10.0.0.1", "status": "up"},
    {"id": "SW1", "device_type": "switch", "ip": "10.0.0.2", "status": "up"},
    {"id": "SW2", "device_type": "switch", "ip": "10.0.0.3", "status": "down"},
]

@app.before_request
def check_api_key():
    if request.path == "/health":
        return None  # health check (no key)
    if not API_KEY or request.headers.get("X-API-Key") != API_KEY:
        return jsonify(error="Unauthorized"), 401 # no key or incorrect key

@app.after_request
def log_request(response): # logs time, path, & status code (key not logged)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')} {request.path} {response.status_code}\n")
    return response

@app.errorhandler(404)
def not_found(error): # error handling
    return jsonify(error="Not found"), 404

# health endpoint
@app.route("/health")
def health():
    return jsonify(status="ok")

# endpoint (full asset)
@app.route("/assets")
def list_assets():
    return jsonify(assets)

# endpoint (one asset)
@app.route("/assets/<asset_id>")
def get_asset(asset_id):
    for asset in assets:
        if asset["id"] == asset_id:
            return jsonify(asset) # known identifier
    return jsonify(error="Asset not found"), 404 # uknown identifier