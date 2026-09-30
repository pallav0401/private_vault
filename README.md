# PyVault - Command-Line Password Vault

**Student:** Pallav Deo (26BAI10204)
**Programming Teacher:** G Prabhu Khanna
**Language:** Python 3

---

## Overview

PyVault is a small command-line password manager written in Python. People often reuse one weak password everywhere because remembering many strong ones is hard. PyVault lets a user keep all their account credentials in one place, protected behind a single **master password**.

On the first run the program asks you to create a master password and creates an encrypted vault file (`my_vault.bin`). On every later run you must enter the same master password to unlock the vault. Once unlocked you can view, add, search and delete saved credentials. The vault is re-written to disk every time it changes, so nothing is lost between sessions.

## Features

- **Master-password protection** - the vault cannot be opened without the correct master password (verified with a SHA-256 hash).
- **Scrambled storage** - the vault file is not stored as readable text; contents are XOR-scrambled with a key derived from the master password.
- **Add** a credential (account name, username/email, password).
- **View** the list of all saved account names.
- **Search** for an account and display its username and password.
- **Delete** a saved account.
- **Persistence** - data is saved to `my_vault.bin` automatically after every add/delete.
- **Input validation & error handling** - empty account names, unknown accounts, invalid menu choices, a blank master password and a wrong master password / corrupted file are all handled with clear messages.

## Technologies / Tools Used

| Tool | Purpose |
|------|---------|
| Python 3 | Programming language |
| `hashlib` (standard library) | SHA-256 hashing of the master password and key derivation |
| `os` (standard library) | Checking whether the vault file exists |
| VS Code | Code editor / integrated terminal |
| Git & GitHub | Version control and submission |

No third-party packages are required.

## Project Structure

```
.
├── VitYarthi_Project_program.py   # Main program (all functions + menu)
├── README.md                      # This file
├── statement.md                   # Problem statement, scope, users, features
├── PyVault_Project_Report.pdf     # Detailed project report
├── docs/                          # Design diagrams (architecture, UML, workflow, storage)
└── screenshots/                   # Program output screenshots
```

`my_vault.bin` is created automatically on first run (do **not** commit it to GitHub - add it to `.gitignore`).

## How to Install and Run

1. Install **Python 3.8 or newer** from <https://www.python.org/downloads/>. Check with:
   ```bash
   python --version
   ```
2. Clone or download this repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
   ```
3. Run the program:
   ```bash
   python VitYarthi_Project_program.py
   ```
4. **First run:** enter a new master password when asked. The vault is created and you are taken to the login prompt.
5. **Later runs:** enter the same master password to unlock the vault, then choose an option from the menu.

### Menu

```
1. Show all saved accounts
2. Add a new password
3. Search for a password
4. Delete a saved password
5. Save and Exit
```

## Instructions for Testing

The project is tested manually through the command line. To reset between tests, delete `my_vault.bin`.

| # | Test | Steps | Expected result |
|---|------|-------|-----------------|
| 1 | First-time setup | Delete `my_vault.bin`, run program, enter a master password | "Vault created successfully!" and `my_vault.bin` appears |
| 2 | Blank master password | On first run press Enter with no text | "Password cannot be blank" and program exits |
| 3 | Correct login | Enter the master password | "Login successful! Vault unlocked." |
| 4 | Wrong login | Enter an incorrect master password | "Access Denied" and program exits |
| 5 | View empty vault | Option 1 on a new vault | "Your vault is currently empty." |
| 6 | Empty account name | Option 2, press Enter for the name | "Account name cannot be empty!" |
| 7 | Add password | Option 2, enter name/username/password | "Password for '<name>' saved successfully!" |
| 8 | Search existing | Option 3, enter a saved name (any case) | Username and password are displayed |
| 9 | Search missing | Option 3, enter an unknown name | "No records found" |
| 10 | Delete existing | Option 4, enter a saved name | "Deleted '<name>' from vault." |
| 11 | Delete missing | Option 4, enter an unknown name | "No records found" |
| 12 | Invalid menu choice | Type `9` or a letter | "Invalid choice!" message |
| 13 | Persistence | Add an entry, choose 5, run again and log in, choose 1 | Entry is still listed |
| 14 | Save and exit | Choose 5 | "Saving data... Locking vault." |

## Screenshots

**1. Login and viewing accounts (empty vault)**
![Login and view](screenshots/01_login_and_view_accounts.png)

**2. Adding a password (with empty-name validation)**
![Add password](screenshots/02_add_password.png)

**3. Searching for a password**
![Search password](screenshots/03_search_password.png)

**4. Deleting a password**
![Delete password](screenshots/04_delete_password.png)

**5. Save and exit**
![Save and exit](screenshots/05_save_and_exit.png)

> The credentials shown in the screenshots are sample data used only for demonstration.

## Security Notes and Known Limitations

PyVault is an educational project. Please be aware of these limitations:

- The XOR "scrambling" hides the file contents from casual viewing but is **not** strong, modern encryption. Do not use PyVault to store real, sensitive passwords.
- The master password is hashed with plain SHA-256 (no salt, no key-stretching).
- The vault is read back using `eval()`, which is unsafe if the file is ever tampered with.
- Passwords are printed in plain text on the terminal when searched.
- All code lives in one file and there are no automated unit tests yet.

See the **Future Enhancements** section of the report for how these can be improved (e.g. `cryptography` library / Fernet, PBKDF2 or bcrypt, JSON storage, modular package, `unittest` tests).

## Author

Pallav Deo - 26BAI10204
