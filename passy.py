import os
import hashlib
import base64
import json
from cryptography.fernet import Fernet

# File paths
PASSWORD_STORE = os.path.expanduser("~/.password_store.json")
MASTER_PASSWORD_HASH = os.path.expanduser("~/.master_password.hash")

# Function to generate a hash of the master password
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Function to generate a key for encryption/decryption
def generate_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

# Function to encrypt the data
def encrypt_data(data: str, key: bytes) -> str:
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data.decode()

# Function to decrypt the data
def decrypt_data(encrypted_data: str, key: bytes) -> str:
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data.encode())
    return decrypted_data.decode()

# Function to save passwords securely
def save_passwords(passwords: dict, key: bytes):
    encrypted_data = encrypt_data(json.dumps(passwords), key)
    with open(PASSWORD_STORE, "w") as f:
        f.write(encrypted_data)

# Function to load passwords securely
def load_passwords(key: bytes) -> dict:
    if not os.path.exists(PASSWORD_STORE):
        return {}
    with open(PASSWORD_STORE, "r") as f:
        encrypted_data = f.read()
    decrypted_data = decrypt_data(encrypted_data, key)
    return json.loads(decrypted_data)

# Function to initialize the password manager
def initialize_password_manager():
    if not os.path.exists(MASTER_PASSWORD_HASH):
        print("Setting up your password manager for the first time...")
        master_password = input("Enter a master password: ")
        confirm_password = input("Confirm your master password: ")
        if master_password != confirm_password:
            print("Passwords do not match.")
            exit(1)
        with open(MASTER_PASSWORD_HASH, "w") as f:
            f.write(hash_password(master_password))
        print("Password manager initialized.")
    else:
        master_password = input("Enter your master password: ")
        stored_hash = open(MASTER_PASSWORD_HASH).read().strip()
        if stored_hash != hash_password(master_password):
            print("Incorrect master password.")
            exit(1)
    return master_password

# Function to add a new password
def add_password(passwords: dict):
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    passwords[website] = {'username': username, 'password': password}
    print("Password added successfully.")

# Function to retrieve a password
def retrieve_password(passwords: dict):
    website = input("Enter the website: ")
    if website in passwords:
        print(f"Username: {passwords[website]['username']}")
        print(f"Password: {passwords[website]['password']}")
    else:
        print("No password found for this website.")

# Main menu function
def show_menu(passwords: dict, key: bytes):
    while True:
        print("\nPassword Manager")
        print("1. Add a password")
        print("2. Retrieve a password")
        print("3. Exit")
        option = input("Choose an option: ")
        if option == "1":
            add_password(passwords)
            save_passwords(passwords, key)
        elif option == "2":
            retrieve_password(passwords)
        elif option == "3":
            print("Exiting password manager.")
            exit(0)
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    master_password = initialize_password_manager()
    key = generate_key(master_password)
    passwords = load_passwords(key)
    show_menu(passwords, key)

