# webhook.py

from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = "YOUR_VERIFY_TOKEN"


@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    print("\n===== WEBHOOK EVENT =====")
    print(data)

    return jsonify({
        "status": "received"
    }), 200


@app.route("/")
def home():
    return {
        "status": "online",
        "service": "WhatsApp Webhook"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
