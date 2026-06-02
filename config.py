import os

# Project Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")
DB_DIR = os.path.join(BASE_DIR, "database")

# Files
CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.csv")
DATABASE_FILE = os.path.join(DB_DIR, "messages.db")

SENT_LOG = os.path.join(LOG_DIR, "sent.log")
FAILED_LOG = os.path.join(LOG_DIR, "failed.log")
DELIVERY_LOG = os.path.join(LOG_DIR, "delivery.log")

# WhatsApp Business API Settings
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"
BUSINESS_ACCOUNT_ID = "YOUR_BUSINESS_ACCOUNT_ID"

# API Endpoint
API_VERSION = "v23.0"

API_URL = (
    f"https://graph.facebook.com/"
    f"{API_VERSION}/"
    f"{PHONE_NUMBER_ID}/messages"
)

# App Settings
DEBUG = True
TIMEOUT = 30

# Message Settings
DEFAULT_LANGUAGE = "en"
MAX_RETRY = 3

# Headers
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
