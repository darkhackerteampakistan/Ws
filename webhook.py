# webhook.py

from flask import Flask, request, jsonify
from config import VERIFY_TOKEN
from database import add_log

app = Flask(__name__)


# ---------------- VERIFY WEBHOOK ----------------
@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Verification failed", 403


# ---------------- RECEIVE EVENTS ----------------
@app.route("/webhook", methods=["POST"])
def receive_webhook():
    data = request.get_json()

    print("\n=== WHATSAPP WEBHOOK EVENT ===")
    print(data)

    # Log event
    add_log("Webhook event received")

    try:
        entry = data.get("entry", [])
        for e in entry:
            changes = e.get("changes", [])
            for change in changes:
                value = change.get("value", {})

                # Incoming messages
                messages = value.get("messages", [])
                for msg in messages:
                    phone = msg.get("from")
                    text = msg.get("text", {}).get("body")

                    add_log(f"Incoming message from {phone}: {text}")

                # Delivery status
                statuses = value.get("statuses", [])
                for status in statuses:
                    msg_id = status.get("id")
                    state = status.get("status")

                    add_log(f"Message {msg_id} status: {state}")

    except Exception as e:
        add_log(f"Webhook error: {str(e)}")

    return jsonify({"status": "received"}), 200


# ---------------- HOME ----------------
@app.route("/")
def home():
    return {
        "status": "running",
        "service": "WhatsApp Webhook"
    }


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
