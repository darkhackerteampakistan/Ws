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
ACCESS_TOKEN = "EAAO9AmflYjoBRrpZBYmMQ1mPZB1uizcyZBECnhZAFJedarnuoxpvslZAhFm2bHodDcETHZAnb0KZASiGSH7C2UP22Xq82uuKGDiVIZBpSiCETG4ZCwJ3D5Iw3ewFPdYaM4ZBGFHIN1TsDdsVxIaQ6Wvz55NV2JcSw0bxySF5pt4uIAFKYmjGr3GtT0yoJVncvPUEknLzud4cdZCFRDwcAOPUTg1pSQX3CaVoG1RjTPD5ZAYDs3sQSN9C7vkiwfYzuhV3DFsCCeiEW2IVPD507j4ZD"
PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"
VERIFY_TOKEN = "YOUR_VERIFY_TOKEN"

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
