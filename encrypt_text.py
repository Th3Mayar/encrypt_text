import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os

# Generate a secret key and save it (only runs once)
def generate_key():
    if not os.path.exists("secretKey.key"):
        key = Fernet.generate_key()
        with open("secretKey.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    with open("secretKey.key", "rb") as key_file:
        return key_file.read()

def encrypt_message():
    key = load_key()
    f = Fernet(key)
    
    message = entry_text.get()
    if not message:
        messagebox.showerror("Error", "Please enter a message to encrypt.")
        return
    
    encrypted_message = f.encrypt(message.encode())
    with open("encryptedMessage.txt", "wb") as enc_file:
        enc_file.write(encrypted_message)
    
    messagebox.showinfo("Success", "Message encrypted and saved successfully!")
    entry_text.delete(0, tk.END)

def decrypt_message():
    if not os.path.exists("encryptedMessage.txt"):
        messagebox.showerror("Error", "No encrypted message found.")
        return
    
    auth_key = entry_key.get()
    if not auth_key:
        messagebox.showerror("Error", "Please enter the authorization key.")
        return
    
    try:
        key = load_key()
        if auth_key.encode() != key[:len(auth_key)]:
            messagebox.showerror("Error", "Authorization failed!")
            return
        
        with open("encryptedMessage.txt", "rb") as enc_file:
            encrypted_message = enc_file.read()

        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message).decode()
        
        messagebox.showinfo("Decrypted Message", decrypted_message)
    except Exception as e:
        messagebox.showerror("Error", "Decryption failed!")

# GUI Setup
generate_key()
root = tk.Tk()
root.title("Message Encryptor & Decryptor")
root.geometry("400x300")
root.configure(bg="#222222")

frame = tk.Frame(root, bg="#333333", padx=20, pady=20)
frame.pack(pady=20)

tk.Label(frame, text="Enter Message:", fg="white", bg="#333333").pack()
entry_text = tk.Entry(frame, width=40)
entry_text.pack(pady=5)

tk.Button(frame, text="Encrypt", command=encrypt_message, bg="#444444", fg="white").pack(pady=5)

tk.Label(frame, text="Enter Key:", fg="white", bg="#333333").pack()
entry_key = tk.Entry(frame, width=40)
entry_key.pack(pady=5)

tk.Button(frame, text="Decrypt", command=decrypt_message, bg="#444444", fg="white").pack(pady=5)

tk.Button(root, text="Exit", command=root.quit, bg="#555555", fg="white").pack(pady=10)

root.mainloop()
