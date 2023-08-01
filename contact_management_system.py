import csv
import os
import logging

CONTACTS_PER_PAGE = 5

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def add_contact():
    unit_numbers = input("Enter Unit Number(s) separated by a comma (no spaces): ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    home_phone = input("Enter Home Phone: ")
    mobile_phone = input("Enter Mobile Phone: ")

    unit_numbers_list = unit_numbers.split(',')
    for unit_number in unit_numbers_list:
        contact = {
            'Unit Number': unit_number,
            'First Name': first_name,
            'Last Name': last_name,
            'Home Phone': home_phone,
            'Mobile Phone': mobile_phone,
        }
        contacts.append(contact)

    if save_contacts_to_file():
        print("Contact(s) added successfully!")

def display_contacts(contacts_to_display):
    total_contacts = len(contacts_to_display)
    if total_contacts == 0:
        print("No contacts found.")
        return

    current_page = 1
    total_pages = (total_contacts - 1) // CONTACTS_PER_PAGE + 1

    while True:
        start_index = (current_page - 1) * CONTACTS_PER_PAGE
        end_index = min(start_index + CONTACTS_PER_PAGE, total_contacts)

        print(f"\n--- Contacts (Page {current_page}/{total_pages}) ---")
        for index in range(start_index, end_index):
            contact = contacts_to_display[index]
            print(f"Unit Number: {contact['Unit Number']}")
            print(f"First Name: {contact['First Name']}")
            print(f"Last Name: {contact['Last Name']}")
            print(f"Home Phone: {contact['Home Phone']}")
            print(f"Mobile Phone: {contact['Mobile Phone']}")
            print()

        print("1. Next Page")
        print("2. Previous Page")
        print("3. Go to Page Number")
        print("4. Return to Main Menu")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            current_page = min(current_page + 1, total_pages)
        elif choice == '2':
            current_page = max(current_page - 1, 1)
        elif choice == '3':
            page_number = int(input(f"Enter the page number (1-{total_pages}): "))
            current_page = max(1, min(page_number, total_pages))
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def save_contacts_to_file():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, "contacts.csv")

    try:
        with open(file_path, mode='w', newline='') as csvfile:
            fieldnames = ['Unit Number', 'First Name', 'Last Name', 'Home Phone', 'Mobile Phone']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contact in contacts:
                writer.writerow(contact)
        return True
    except Exception as e:
        log_error(e)
        return False

def log_error(error):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(script_directory, "log.txt")

    logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s - %(message)s')
    logging.error(str(error))

def load_contacts_from_file(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts.append({
                    'Unit Number': row['Unit Number'],
                    'First Name': row['First Name'],
                    'Last Name': row['Last Name'],
                    'Home Phone': row['Home Phone'],
                    'Mobile Phone': row['Mobile Phone'],
                })
        return True
    except Exception as e:
        log_error(e)
        return False

def search_contacts():
    search_term = input("Enter search term: ")

    search_results = []
    for contact in contacts:
        if search_term.lower() == contact['Unit Number'].lower() or \
           search_term.lower() == (contact['First Name'] + ' ' + contact['Last Name']).lower():
            search_results.append(contact)

    display_contacts(search_results)

def edit_contact():
    unit_number_to_edit = input("Enter the Unit Number of the contact you want to edit: ")

    found_contact = None
    for contact in contacts:
        if contact['Unit Number'].lower() == unit_number_to_edit.lower():
            found_contact = contact
            break

    if found_contact is None:
        print("Contact not found.")
        return

    print("\n--- Current Contact Information ---")
    print(f"Unit Number: {found_contact['Unit Number']}")
    print(f"First Name: {found_contact['First Name']}")
    print(f"Last Name: {found_contact['Last Name']}")
    print(f"Home Phone: {found_contact['Home Phone']}")
    print(f"Mobile Phone: {found_contact['Mobile Phone']}")

    print("\n--- Editing Contact ---")
    print("1. First Name")
    print("2. Last Name")
    print("3. Home Phone")
    print("4. Mobile Phone")
    print("5. Return to Main Menu")
    choice = input("Enter the field number to edit (1/2/3/4/5): ")

    if choice == '1':
        new_first_name = input("Enter new First Name: ")
        found_contact['First Name'] = new_first_name
    elif choice == '2':
        new_last_name = input("Enter new Last Name: ")
        found_contact['Last Name'] = new_last_name
    elif choice == '3':
        new_home_phone = input("Enter new Home Phone: ")
        found_contact['Home Phone'] = new_home_phone
    elif choice == '4':
        new_mobile_phone = input("Enter new Mobile Phone: ")
        found_contact['Mobile Phone'] = new_mobile_phone
    elif choice == '5':
        return
    else:
        print("Invalid choice. Please try again.")

    if save_contacts_to_file():
        print("Contact updated successfully!")

def press_any_key_to_continue():
    input("Press Enter to continue...")

if __name__ == "__main__":
    # Modify the file_path to handle the script running as an EXE
    if getattr(sys, 'frozen', False):
        # When running as EXE, the script is frozen
        script_directory = os.path.dirname(sys.executable)
    else:
        # When running as a Python script, use the current script directory
        script_directory = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(script_directory, "contacts.csv")

    # Initialize the contacts list before calling functions
    contacts = []

    # Check if the CSV file exists and load contacts from it
    if os.path.exists(file_path):
        if not load_contacts_from_file(file_path):
            print("Failed to load contacts from file. Starting with an empty contact list.")
    else:
        print("No contacts file found. Starting with an empty contact list.")

    # Display ASCII art
    ascii_art = """
 _____             _             _    ___  ___                                  
/  __ \           | |           | |   |  \/  |                                  
| /  \/ ___  _ __ | |_ __ _  ___| |_  | .  . | __ _ _ __   __ _  __ _  ___ _ __ 
| |    / _ \| '_ \| __/ _` |/ __| __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| \__/\ (_) | | | | || (_| | (__| |_  | |  | | (_| | | | | (_| | (_| |  __/ |   
 \____/\___/|_| |_|\__\__,_|\___|\__| \_|  |_/\__,_|_| |_|\__,_|\__, |\___|_|   
                                                                 __/ |          
                                                                |___/
                                          Coded By: athrtyfrck 2023    
   """
    print(ascii_art)
    press_any_key_to_continue()

    while True:
        clear_screen()
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Edit Contacts")
        print("3. Display Contacts")
        print("4. Search Contacts")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            clear_screen()
            add_contact()
        elif choice == '2':
            clear_screen()
            edit_contact()
        elif choice == '3':
            clear_screen()
            display_contacts(contacts)
        elif choice == '4':
            clear_screen()
            search_contacts()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")