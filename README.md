```
# Contact Management System

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

The Contact Management System is a simple Python program that allows users to manage their contacts. It provides functionality to add, edit, search, and display contacts. The contacts are stored in a CSV file for easy data persistence.

## Features

- Add contacts: Users can add new contacts with their Unit Number, First Name, Last Name, Home Phone, and Mobile Phone.
- Edit contacts: Users can edit existing contacts' information like First Name, Last Name, Home Phone, and Mobile Phone.
- Display contacts: The program displays contacts in a paginated manner, allowing the user to navigate through the list easily.
- Search contacts: Users can search for contacts by Unit Number or by First Name and Last Name combination.

## Requirements

- Python 3.7 or above

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/athrtyfrck/contact-management-system.git
```

2. Change the working directory:

```bash
cd contact-management-system
```

3. Run the Contact Management System:

```bash
python contact_management_system.py
```

## Usage

1. Upon running the program, you will see an ASCII art representing the Contact Management System.

2. Follow the on-screen menu to perform various actions:

   - To add a new contact, choose option 1 and enter the required information.
   - To edit an existing contact, choose option 2 and follow the prompts.
   - To display the contacts, choose option 3.
   - To search for contacts, choose option 4 and enter the search term.
   - To exit the program, choose option 5.

3. The contacts are automatically saved to the `contacts.csv` file in the program's directory.

## Changing the ASCII Art

If you want to change the ASCII art displayed when the program starts, open `contact_management_system.py` in a text editor. Look for the variable `ascii_art` you can replace it with your desired ASCII art.

## License

This project is licensed under the MIT License.

## Author

Coded By: athrtyfrck (GitHub: athrtyfrck)

Feel free to contribute and improve the Contact Management System. If you encounter any issues or have suggestions, please feel free to create an issue or submit a pull request.

Happy managing your contacts!