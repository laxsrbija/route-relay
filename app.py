from flask import Flask, request, jsonify
import requests
import json
import logging
import os

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

try:
    with open('config.json') as f:
        config = json.load(f)
except FileNotFoundError:
    logging.error("Configuration file not found")
    raise
except json.JSONDecodeError:
    logging.error("Error decoding configuration file")
    raise

def forward_request(endpoint_config):
    url = endpoint_config["url"]
    headers = endpoint_config.get("headers", {})
    body = endpoint_config.get("body", {})

    try:
        response = requests.post(url, json=body, headers=headers)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Request to {url} failed: {e}")
        return {"error": str(e)}, 500

@app.route('/<path:input>')
def show_path(input):
    endpoint_config = config.get('/' + input)
    if not endpoint_config:
        return jsonify({"error": "Endpoint not found"}), 404

    return forward_request(endpoint_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)