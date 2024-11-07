import os
import time
import jwt
import json
from tkinter import *
import mysql.connector as my
from tkinter import messagebox as msg
from cryptography.fernet import Fernet
from datetime import datetime, timedelta

# Generate a key for encryption (Only once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt and Decrypt data (for secure token storage)
def encrypt_token(token):
    f = Fernet(load_key())
    encrypted_token = f.encrypt(token.encode())
    return encrypted_token

def decrypt_token(encrypted_token):
    f = Fernet(load_key())
    decrypted_token = f.decrypt(encrypted_token).decode()
    return decrypted_token

# Create JWT token
def create_jwt_token(username):
    expiration_time = datetime.utcnow() + timedelta(minutes=2)  # 2 minutes expiry
    payload = {
        'username': username,
        'exp': expiration_time
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    encrypted_token = encrypt_token(token)
    
    # Store token in a file securely
    with open(os.path.expanduser("~/Desktop/token.txt"), 'wb') as f:
        f.write(encrypted_token)
    
    return token

# Check if token is expired
def is_token_expired():
    try:
        with open(os.path.expanduser("~/Desktop/token.txt"), 'rb') as f:
            encrypted_token = f.read()
        token = decrypt_token(encrypted_token)
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        if datetime.utcnow() > datetime.utcfromtimestamp(payload['exp']):
            return True
        return False
    except Exception as e:
        return True

# Destroy the token upon logout
def logout():
    if os.path.exists(os.path.expanduser("~/Desktop/token.txt")):
        os.remove(os.path.expanduser("~/Desktop/token.txt"))
    msg.showinfo("Logout", "You have been logged out successfully!")

# Update session time and renew token
def update_session_time():
    if not is_token_expired():
        with open(os.path.expanduser("~/Desktop/token.txt"), 'rb') as f:
            encrypted_token = f.read()
        token = decrypt_token(encrypted_token)
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        # Refresh token expiration time
        payload['exp'] = datetime.utcnow() + timedelta(minutes=2)
        new_token = jwt.encode(payload, 'secret', algorithm='HS256')
        encrypted_new_token = encrypt_token(new_token)
        
        with open(os.path.expanduser("~/Desktop/token.txt"), 'wb') as f:
            f.write(encrypted_new_token)

# Function to create homepage
def homepage():
    root = Tk()
    root.title("CENTRALIZED HOSPITAL MANAGEMENT FOR PATIENTS")
    root.geometry("1600x1600")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0,y=0)

    label2 = Label(root, text="CENTRALIZED HOSPITAL MANAGEMENT FOR PATIENTS", fg="black", bg="#856ff8", borderwidth=5, width=50)
    label2.pack(pady=50)
    label2.configure(font=("Algerian", 17, "bold"))

    def tech():
        root.destroy()
        alll()

    b = Button(root, text="Indian Health Department Login", borderwidth=5, width=35, command=tech)
    b.place(x=600, y=200)
    b.configure(font=("Castellar", 10, "bold"))

    def logg():
        root.destroy()
        hoslog()

    b1 = Button(root, text="Hospital Login", borderwidth=5, width=35, command=logg)
    b1.place(x=600, y=300)
    b1.configure(font=("Castellar", 10, "bold"))

    def logg1():
        root.destroy()
        humanlog()

    b2 = Button(root, text="Human Login", borderwidth=5, width=35, command=logg1)
    b2.place(x=600, y=400)
    b2.configure(font=("Castellar", 10, "bold"))

    root.mainloop()

# Function for Indian Health Department Login
def alll():
    root = Tk()
    root.geometry("1600x1600")
    root.title("Indian Health Department Login")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file="IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0, y=0)
    m = Label(root, text="INDIAN HEALTH DEPARTMENT", fg="black", bg="blue", borderwidth=5, width=50)
    m.place(x=400, y=50)
    m.configure(font=("Algerian", 17, "bold"))
    w = Label(root, text="User Name", borderwidth=5, width=10, font=("Castellar", 10, "bold"), bg="#856ff8")
    w.place(x=500, y=200)
    z = Label(root, text="Password", borderwidth=5, width=10, bg="#856ff8", font=("Castellar", 10, "bold"))
    z.place(x=500, y=300)
    t = Entry(root, borderwidth=5, width=50, font=("Times New Roman", 10, "bold"))
    t.place(x=700, y=200)
    t1 = Entry(root, borderwidth=5, width=50, show="*", font=("Times New Roman", 10, "bold"))
    t1.place(x=700, y=300)

    def llen():
        con = my.connect(host="localhost", user="root", password="22MIS0162", database="hospital")
        cur = con.cursor()
        cur.execute("select * from login where username='" + t.get() + "' and password='" + t1.get() + "'")
        d = cur.fetchall()
        if d:
            msg.showinfo("Login Status", "Login Successfully " + t.get())
            root.destroy()
            adminpage()  # Proceed to admin page
        else:
            msg.showinfo("Login Status", "Username/Password Invalid")

    b = Button(root, text="Submit", borderwidth=5, width=10, command=llen)
    b.place(x=700, y=400)

    def back():
        root.destroy()
        homepage()

    b1 = Button(root, text="Home", borderwidth=5, width=10, command=back)
    b1.place(x=800, y=400)

    root.mainloop()

# Function for hospital login page
def hoslog():
    root = Tk()
    root.geometry("1600x1600")
    root.title("Hospital Login")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file="IMG_4557.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place(x=0, y=0)

    label2 = Label(root, text="Hospital Login", fg="black", bg="#856ff8", borderwidth=5, width=50)
    label2.pack(pady=50)
    label2.configure(font=("Algerian", 17, "bold"))

    def login():
        con = my.connect(host="localhost", user="root", password="22MIS0162", database="hospital")
        cur = con.cursor()
        username = t.get()
        password = t1.get()
        cur.execute("select * from login where username='" + username + "' and password='" + password + "'")
        d = cur.fetchall()
        if d:
            msg.showinfo("Login Status", "Login Successfully " + username)
            create_jwt_token(username)  # Generate JWT Token and store it securely
            root.destroy()
            adminpage()  # Proceed to the next page
        else:
            msg.showinfo("Login Status", "Username/Password Invalid")

    w = Label(root, text="User Name", borderwidth=5, width=10, font=("Castellar", 10, "bold"), bg="#856ff8")
    w.place(x=500, y=200)
    z = Label(root, text="Password", borderwidth=5, width=10, bg="#856ff8", font=("Castellar", 10, "bold"))
    z.place(x=500, y=300)
    t = Entry(root, borderwidth=5, width=50, font=("Times New Roman", 10, "bold"))
    t.place(x=700, y=200)
    t1 = Entry(root, borderwidth=5, width=50, show="*", font=("Times New Roman", 10, "bold"))
    t1.place(x=700, y=300)

    b = Button(root, text="Submit", borderwidth=5, width=10, command=login)
    b.place(x=700, y=400)

    def back():
        root.destroy()
        homepage()

    b1 = Button(root, text="Home", borderwidth=5, width=10, command=back)
    b1.place(x=800, y=400)

    root.mainloop()

# This would be the function for the admin page
def adminpage():
    # Implement the necessary admin page features and functionality here
    pass

# Start the app
homepage()
