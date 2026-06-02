# config.py

import os

# Project Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")
DB_DIR = os.path.join(BASE_DIR, "database")

# Files
CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.csv")
DATABASE_FILE = os.path.join(DB_DIR, "messages.db")

APP_LOG = os.path.join(LOG_DIR, "app.log")
DELIVERY_LOG = os.path.join(LOG_DIR, "delivery.log")

# WhatsApp Business Platform
ACCESS_TOKEN = "EAAOdpIDDFnoBRielhQpMFg21WOvT8reDmmBEHKZCFSENndV0CyODNUUpHTijPBAEfloZAkfRE5ZCZBt40hovFdZAxfhsImZCSsEfYIFAtrArpypCX7IljZABOZBPPszmBkvt3QqEZAdx7qZBb3BZBP7ECDFbxtHryKuZBeZBqqFzJjxPvW15GkJZBrKJJpU7vgBQpgZAbr8cJPVipgojZBGKtZAzMEwkJa23Iog2ZAWbCHDnlpsp6R3NJ0azaAlhrMZBrbJLA8MNjq2FfgiD9enBNnZBCTTXzz6n81vC"
PHONE_NUMBER_ID = "1138318886029704"
VERIFY_TOKEN = "Rifat_2026_WhatsApp_X9K7P2"

# Meta Graph API
API_VERSION = "v23.0"

API_BASE_URL = (
    f"https://graph.facebook.com/"
    f"{API_VERSION}"
)

# App Settings
DEBUG = True
TIMEOUT = 30

# Ensure directories exist
for directory in [DATA_DIR, LOG_DIR, DB_DIR]:
    os.makedirs(directory, exist_ok=True)
