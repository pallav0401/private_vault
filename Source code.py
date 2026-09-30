# Program: Password Vault
# Student: Pallav Deo (26BAI10204)
#Programming Teacher: G Prabhu Khanna

import hashlib
import os

VAULT_FILE = "my_vault.bin"


def get_hash(txt):
    return hashlib.sha256(txt.encode()).hexdigest()


def scramble(data, key):
    k = hashlib.sha256(key.encode()).digest()
    out = bytearray()
    for i in range(len(data)):
        out.append(data[i] ^ k[i % len(k)])
    return bytes(out)


def save_vault(db, key, h):
    raw = f"{h}||{str(db)}"
    enc = scramble(raw.encode("utf-8"), key)
    with open(VAULT_FILE, "wb") as f:
        f.write(enc)


def load_vault(key):
    if not os.path.exists(VAULT_FILE):
        return None, None
    with open(VAULT_FILE, "rb") as f:
        enc = f.read()
    try:
        dec = scramble(enc, key).decode("utf-8")
        parts = dec.split("||", 1)
        return parts[0], eval(parts[1])
    except:
        return None, None


def main():
    print("      Welcome to My Password Vault (PyVault)     ")

    if not os.path.exists(VAULT_FILE):
        print("\nLooks like this is your first time setting up!")
        pwd = input("Create a Master Password for your vault: ").strip()
        if not pwd:
            print("Password cannot be blank. Program exiting.")
            return

        h_val = get_hash(pwd)
        save_vault({}, pwd, h_val)
        print("Vault created successfully! Restarting for login...\n")

    print("\n--- LOGIN ---")
    pwd = input("Enter Master Password: ").strip()
    st_hash, db = load_vault(pwd)

    if st_hash is None or get_hash(pwd) != st_hash:
        print("\n[!] Wrong Master Password or corrupted file! Access Denied.")
        return

    print("\nLogin successful! Vault unlocked.")

    run = True
    while run:
        print("\n==================================================")
        print("1. Show all saved accounts")
        print("2. Add a new password")
        print("3. Search for a password")
        print("4. Delete a saved password")
        print("5. Save and Exit")

        ch = input("Select an option (1-5): ").strip()

        if ch == "1":
            if not db:
                print("\nYour vault is currently empty.")
            else:
                print("\nSaved Accounts:")
                for idx, name in enumerate(db.keys(), 1):
                    print(f"  {idx}. {name}")

        elif ch == "2":
            acc = (
                input("Enter Account/App Name (e.g. Gmail, Instagram): ")
                .strip()
                .lower()
            )
            if not acc:
                print("Account name cannot be empty!")
                continue
            usr = input("Enter Username/Email: ").strip()
            p = input("Enter Password: ").strip()
            db[acc] = {"username": usr, "password": p}
            save_vault(db, pwd, st_hash)
            print(f"\nPassword for '{acc}' saved successfully!")

        elif ch == "3":
            acc = input("Enter Account Name to lookup: ").strip().lower()
            if acc in db:
                info = db[acc]
                print(f"\n--- Account Details for '{acc.upper()}' ---")
                print(f"Username / Email : {info['username']}")
                print(f"Password         : {info['password']}")
            else:
                print(f"\n[!] No records found for '{acc}'.")

        elif ch == "4":
            acc = input("Enter Account Name to delete: ").strip().lower()
            if acc in db:
                del db[acc]
                save_vault(db, pwd, st_hash)
                print(f"\n[+] Deleted '{acc}' from vault.")
            else:
                print(f"\n[!] No records found for '{acc}'.")

        elif ch == "5":
            print("\nSaving data... Locking vault.")
            run = False

        else:
            print("\nInvalid choice! Please type a number from 1 to 5.")


if __name__ == "__main__":
    main()
