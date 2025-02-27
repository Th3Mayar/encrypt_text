from cryptography.fernet import Fernet
import os

# Generate a secret key and save it (only runs once)
def generateKey():
    if not os.path.exists("secretKey.key"):
        key = Fernet.generate_key()
        with open("secretKey.key", "wb") as keyFile:
            keyFile.write(key)

# Load the key from the file
def loadKey():
    with open("secretKey.key", "rb") as keyFile:
        return keyFile.read()

# Encrypt a message and save it
def encryptMessage():
    key = loadKey()
    f = Fernet(key)

    message = input("Enter the text to encrypt: ")
    encryptedMessage = f.encrypt(message.encode())

    with open("encryptedMessage.txt", "wb") as encFile:
        encFile.write(encryptedMessage)

    print("\nMessage encrypted and saved successfully!")

# Decrypt the message by requesting authorization
def decryptMessage():
    if not os.path.exists("encryptedMessage.txt"):
        print("No encrypted message found.")
        return

    authKey = input("\nEnter authorization key to decrypt: ")

    try:
        key = loadKey()
        if authKey.encode() != key[:len(authKey)]:  # Basic auth check
            print("Authorization failed!")
            return
        
        with open("encryptedMessage.txt", "rb") as encFile:
            encryptedMessage = encFile.read()

        f = Fernet(key)
        decryptedMessage = f.decrypt(encryptedMessage).decode()
        
        print("\nDecrypted Message:", decryptedMessage)

    except Exception as e:
        print("Decryption failed!", str(e))

# Main menu
def main():
    generateKey()

    while True:
        print("\n1. Encrypt a Message")
        print("2. Decrypt a Message")
        print("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            encryptMessage()
        elif choice == "2":
            decryptMessage()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
