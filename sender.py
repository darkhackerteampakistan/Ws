# sender.py

from config import API_URL, ACCESS_TOKEN


class WhatsAppClient:
    def __init__(self):
        self.api_url = API_URL
        self.token = ACCESS_TOKEN

    def check_configuration(self):
        if not self.token or self.token == "YOUR_ACCESS_TOKEN":
            return False, "ACCESS_TOKEN is not configured"

        return True, "Configuration looks valid"

    def get_status(self):
        ok, message = self.check_configuration()

        return {
            "configured": ok,
            "message": message,
            "api_url": self.api_url
        }


if __name__ == "__main__":
    client = WhatsAppClient()

    status = client.get_status()

    print("\n=== WhatsApp API Status ===")
    print(f"Configured : {status['configured']}")
    print(f"Message    : {status['message']}")
    print(f"API URL    : {status['api_url']}")
