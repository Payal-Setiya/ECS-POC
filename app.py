from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    env_name = os.getenv("ENV_NAME", "dev")
    return f"Python Flask App running on ECS Fargate-Environment: {env_name}"

@app.route("/health")
def health():
    return jsonify(status="UP"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
