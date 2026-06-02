import os
from datetime import datetime

CONTACTS_FILE = "data/contacts.csv"
LOG_FILE = "logs/app.log"


def ensure_dirs():
    os.makedirs("data", exist_ok=True)
    os.makedirs("logs", exist_ok=True)


def write_log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {message}\n")


def show_contacts():
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts file found.")
        return

    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("\n=== CONTACTS ===")
    for i, line in enumerate(lines, start=1):
        print(f"{i}. {line.strip()}")


def show_logs():
    if not os.path.exists(LOG_FILE):
        print("No logs available.")
        return

    print("\n=== LOGS ===")
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        print(f.read())


def main():
    ensure_dirs()

    while True:
        print("\n===== WhatsApp Business Manager =====")
        print("1. Show Contacts")
        print("2. Show Logs")
        print("3. Exit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            show_contacts()

        elif choice == "2":
            show_logs()

        elif choice == "3":
            write_log("Application closed")
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
