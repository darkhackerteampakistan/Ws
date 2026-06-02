# app.py

from database import (
    init_database,
    add_contact,
    get_contacts,
    add_log,
    get_logs
)


def show_contacts():
    contacts = get_contacts()

    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n=== CONTACTS ===")

    for contact in contacts:
        cid, name, phone = contact
        print(f"[{cid}] {name} - {phone}")


def add_new_contact():
    name = input("Name : ").strip()
    phone = input("Phone: ").strip()

    add_contact(name, phone)
    add_log(f"Contact added: {phone}")

    print("\nContact saved successfully.")


def show_logs_menu():
    logs = get_logs()

    print("\n=== LOGS ===")

    if not logs:
        print("No logs available.")
        return

    for log in logs:
        lid, event, created_at = log
        print(f"[{lid}] {created_at}")
        print(f"     {event}")
        print()


def main():
    init_database()

    while True:
        print("\n==========================")
        print(" WhatsApp Business Manager")
        print("==========================")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Show Logs")
        print("4. Exit")

        choice = input("\nSelect Option: ").strip()

        if choice == "1":
            add_new_contact()

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            show_logs_menu()

        elif choice == "4":
            add_log("Application closed")
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    main()
