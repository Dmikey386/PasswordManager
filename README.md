# Password Manager

## Overview
The **Password Manager** is a simple and secure password management tool built using Python and Tkinter. It provides features such as password generation, storage, retrieval, and clipboard copying for easy use. The application securely saves credentials in a JSON file and includes a user-friendly graphical interface.

## Skills Used
### **PYTHON**
- Installing and working with Python **packages** and **documentation** (`tkinter`, `json`, `random`, `pyperclip`)
- **Interactive GUI Development** – Using `tkinter` for user-friendly UI design
- **Data management** – JSON manipulation for structured storage and retrieval
- **Error handling** – Using try-except blocks for robust exception management
- **File handling** – Reading, writing, and updating JSON files

### **GIT**
- **Repository creation** – Setting up and managing version control
- **Branching and merging** – Handling feature branches efficiently
- **Pushing to repository** – Committing and pushing code to remote repositories
- **Handling merge conflicts** – Resolving conflicts during collaborative development

### **SOFTWARE DEVELOPMENT**
- **Event-driven programming** – Implementing button-click handlers and user interactions
- **Clipboard automation** – Using `pyperclip` for automatic password copying
- **Modular programming** – Writing reusable functions for better maintainability
- **Code documentation** – Writing comments and docstrings for clarity

## Features
- **Password Generator**: Creates strong, random passwords with a mix of letters, numbers, and symbols.
- **Save Credentials**: Stores usernames and passwords for various applications securely in a JSON file.
- **Search Functionality**: Allows users to retrieve stored credentials by entering an application name.
- **Clipboard Copying**: Automatically copies generated passwords to the clipboard.
- **User-Friendly Interface**: Built using Tkinter for easy interaction.

## Requirements
Ensure you have the following dependencies installed before running the application:

- Python 3.x
- Tkinter (comes pre-installed with Python)
- `pyperclip` (for clipboard functionality)

To install missing dependencies, run:
```bash
pip install pyperclip
```

## Installation & Usage

1. Clone the repository or download the script.
```bash
git clone https://github.com/your-repository/password-manager.git
cd password-manager
```

2. Run the application.
```bash
python password_manager.py
```

3. The GUI will open, allowing you to:
   - Generate secure passwords
   - Save new credentials
   - Search for stored passwords

## File Structure
```
password-manager/
│── password_manager.py    # Main script
│── passwords.json         # JSON storage for passwords (auto-generated)
│── logo.png               # Application logo
```

## How It Works
### 1. Generate a Password
Click the "Generate Password" button to create a strong password, which is automatically inserted into the password field.

### 2. Save a Password
- Enter the website/application name.
- Enter the username/email and generated password.
- Click "Add Password" to store it securely in `passwords.json`.

### 3. Retrieve a Password
- Enter the application name.
- Click "Search" to retrieve stored credentials.

### 4. Copy to Clipboard
When saving a password, it is automatically copied to the clipboard for easy pasting.

## JSON Storage Format
Passwords are stored in a JSON file with the following structure:
```json
{
    "ApplicationName": {
        "user": "example@email.com",
        "password": "GeneratedPassword123!"
    }
}
```


## Disclamer This was an application for my personal education journey and experimenting with python development to further my experience as a data engineer

---
**Developed by Michael Dodd**

