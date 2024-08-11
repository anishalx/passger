# 🛡️ Passger 🛡️
A simple and secure password manager implemented in Python. This application allows users to add and retrieve passwords for various websites, using cryptographic hash functions to securely store and verify passwords

- - -
## 🚀 Features

- **🔒 Secure Storage**: Passwords are hashed using the robust SHA-256 algorithm, keeping your secrets safe.
- **🎨 Elegant Interface**: Navigate effortlessly through a clean and intuitive text-based menu.
- **🌍 Cross-Platform**: Runs seamlessly on all Linux distributions, including the mighty Arch Linux.

- - -
## 📥 Installation

### 🛠️ Prerequisites

Ensure you have Python 3 installed. Check by running:

```bash
sudo apt install python3

python3 --version 
```

- - -
🚀 Quick Start

- **1**. Clone the Repository.
         Grab the code from GitHub and navigate into the project directory:
  ```bash
  sudo apt install git
  ```
  ```bash
  git clone https://github.com/anishalx/passger.git
  
  cd passger && ls
  ```
- **2**. Run the Script.
         We’ve included a Bash script for a smooth launch:
  ```bash
  chmod +x passger.sh
  
  ./passger.sh
  ```
  This will start the password_manager.py script and open the password manager interface.
- - -

## 🧩 How It Works
- **🔐 Password Hashing**: We use SHA-256 to hash your passwords. This way, your sensitive data is never stored in plaintext, reducing the risk of exposure.
- **📦 File Storage**:Passwords are hashed using SHA-256 and then encrypted before being stored in 'passwords.json'.

- - -
## 🎨 Usage
   Once you launch the application, you'll be greeted with a stylish menu:
- **1. ✨ Add a New Password**:Enter the website name and your password. We’ll securely hash it and save it for future use.
- **2. 🔍 Retrieve a Password**:Input the website name to check if a password is stored. Note: For your security, passwords are not displayed in plaintext.
- **3. 🚪 Exit**:Close the application when you’re done.

- - -

## 📋 Example
   Launch the application:
   
      [NOTE:- Don't forget your master password, if you forget it, you will not be able to recover it.]
   
   <p align="center"><img src="https://www.imghost.net/ib/DdZGpw7QSI4nasr_1723372409.png" alt="Screenshot from 2024-08-11 16-02-24.png" width="50%" height="30%"/></p> 

<b>✨ Add a New Password</b>
  <p align="center"><img src="https://www.imghost.net/ib/aVFFMfqk4NysMhu_1723398125.png" width="50%" height="30%"/></p> 

<b>🔍 Retrieve a Password</b>
  <p align="center"><img src="https://www.imghost.net/ib/NMjixGJiksP1yAH_1723398491.png" width="50%" height="30%"/></p> 

<b>🚪 Exit</b>
  <p align="center"><img src="https://www.imghost.net/ib/nCZ8XCjB0isYJXA_1723398352.png" width="50%" height="30%"/></p> 
  
- - -
### 📝 License

<b>This project is licensed under the MIT License - see the LICENSE file for details.</b>
### 📧 Contact

<b>Feel free to reach out if you have any questions or suggestions.</b>
- **Email**: anishalx7@gmail.com
- **Twitter**: anishalx7

- - -
