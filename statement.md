# Project Statement - PyVault (Password Vault)

**Student:** Pallav Deo (26BAI10204)
**Programming Teacher:** G Prabhu Khanna

## Problem Statement

Today almost everyone has dozens of online accounts (email, social media, banking, shopping, college portals). Remembering a strong, unique password for each one is very difficult, so people commonly reuse the same simple password everywhere, write passwords on paper, or keep them in plain text files or notes apps. If one of these is leaked or found, all of the person's accounts are at risk.

There is a need for a simple tool that lets a user store many account credentials in **one place**, protected by **one master password**, without keeping them as readable plain text.

## Scope of the Project

**In scope**

- A command-line (terminal) application written in Python 3.
- Creating a vault protected by a master password on first use.
- Authenticating the user with the master password on every later run.
- Storing, listing, searching and deleting account credentials (account name, username/email, password).
- Saving the vault to a local binary file (`my_vault.bin`) in scrambled form so that it is not readable as plain text.
- Input validation and clear error messages for wrong passwords, empty inputs, unknown accounts and invalid menu choices.

**Out of scope (for this version)**

- Graphical user interface or web/mobile version.
- Cloud sync, multi-user accounts or password sharing.
- Automatic password generation or password-strength checking.
- Industry-grade encryption and account recovery if the master password is forgotten.

## Target Users

- Students and individuals who want a simple, offline way to keep their account passwords together.
- Beginners learning Python who want to see a practical example of hashing, file handling and menu-driven programs.
- Instructors evaluating the application of programming concepts in a real-world context.

## High-Level Features

1. **Master password setup and login** - first-run vault creation and SHA-256 hash verification on every login.
2. **Add password** - save an account name, username/email and password.
3. **Show all accounts** - list the names of all saved accounts.
4. **Search password** - look up the username and password for an account (case-insensitive).
5. **Delete password** - remove a saved account from the vault.
6. **Scrambled persistent storage** - the vault is stored in `my_vault.bin` and updated automatically after every change.
7. **Validation and error handling** - blank inputs, wrong master password, corrupted file and invalid choices are handled gracefully.

