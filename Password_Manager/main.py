import json
from pyperclip import copy
from random import choice, randint, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from tkinter import *
from tkinter import messagebox


# ---------------------------- SEARCH DATA -------------------------------------- #
def search_data():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError as error_msg:
        messagebox.showerror(title="File Not Found", message=f"{error_msg}")
    else:
        website = website_entry.get()
        if website in data:
            email_user = data[website]["Email/Username"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email/Username: {email_user}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Not Found", message=f"No credentials exist for {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    lowercase = [choice(ascii_lowercase) for _ in range(randint(4, 8))]
    uppercase = [choice(ascii_uppercase) for _ in range(randint(2, 4))]
    numbers = [choice(digits) for _ in range(randint(2, 4))]
    symbols = [choice(punctuation) for _ in range(randint(1, 3))]

    pwd = lowercase + uppercase + numbers + symbols
    pwd = list(pwd)
    shuffle(pwd)
    pwd = ''.join(pwd)
    password_entry.delete(0, END)
    password_entry.insert(0, pwd)

    copy(pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_credentials():
    website = website_entry.get()
    email_user = email_user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email_user) == 0 or len(password) == 0:
        # ALERT FOR WHEN FIELDS ARE EMPTY
        messagebox.showwarning(title="OOPS", message="Please don't leave any fields empty!")
    else:
        # CONFIRMATION MESSAGE
        confirm = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email_user}\n"
                                                                f"Password: {password}\nIs it OK to save?")
        if confirm:
            # GET NEW CREDENTIALS FROM USER
            credentials = {website: {
                "Email/Username": email_user,
                "Password": password
            }
            }
            try:
                with open("data.json", "r") as data_file:
                    # READING OLD DATA
                    data = json.load(data_file)
            except FileNotFoundError:
                # IF FILE DOES NOT EXIST, CREATE ONE
                with open("data.json", "w") as data_file:
                    json.dump(credentials, data_file, indent=4)
            else:
                # IF FILE DOES EXIST, UPDATE IT
                data.update(credentials)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                # CLEARING ENTRY FIELDS
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# WINDOW
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# LOGO
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, columnspan=3, row=0)

# WEBSITE LABEL
website_label = Label(text="Website", font=("JetBrains Mono", 8, "bold"))
website_label.grid(column=0, row=1)

# WEBSITE ENTRY
website_entry = Entry(relief="groove")
website_entry.grid(column=1, row=1, sticky="e", padx=(0, 10))
website_entry.focus()

# SEARCH
search_button = Button(text="Search", font=("JetBrains Mono", 8, "bold"), command=search_data)
search_button.grid(column=2, row=1, sticky="we")

# EMAIL/USERNAME LABEL
email_user_label = Label(text="Email/Username", font=("JetBrains Mono", 8, "bold"))
email_user_label.grid(column=0, row=2)

# EMAIL/USERNAME ENTRY
email_user_entry = Entry(width=20, relief="groove")
email_user_entry.grid(column=1, columnspan=2, row=2, sticky="ew", pady=10)
email_user_entry.insert(0, "mikemendez@mail.com")

# PASSWORD LABEL
password_label = Label(text="Password", font=("JetBrains Mono", 8, "bold"))
password_label.grid(column=0, row=3)

# PASSWORD ENTRY
password_entry = Entry(width=20, relief="groove")
password_entry.grid(column=1, row=3, sticky="e", padx=(0, 10))

# GENERATE PASSWORD BUTTON
generate_pwd_button = Button(text="Generate Password", font=("JetBrains Mono", 8, "bold"), command=generate_pwd)
generate_pwd_button.grid(column=2, row=3, sticky="we", pady=10)

# ADD BUTTON
add_credentials_button = Button(text="Add", font=("JetBrains Mono", 8, "bold"), command=add_credentials)
add_credentials_button.grid(column=1, columnspan=2, row=4, sticky="ew")

window.mainloop()
