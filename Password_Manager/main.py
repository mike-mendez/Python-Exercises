from os.path import exists
from pandas import concat, DataFrame, read_csv
from pyperclip import copy
from random import choice, randint, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from tkinter import *
from tkinter import messagebox


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
        # GET NEW CREDENTIALS FROM USER AND ADD TO EXISTING DATA
        credentials = {
            website_label["text"]: [website],
            email_user_label["text"]: [email_user],
            password_label["text"]: [password],
        }
        # CONFIRMATION MESSAGE
        confirm = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email_user}\n"
                                                                f"Password: {password}\nIs it OK to save?")
        if confirm:
            if exists("data.csv"):  # CHECKING TO SEE IF DATA EXISTS
                old_data = read_csv("data.csv")
                new_data = DataFrame(credentials)
                # CONCAT NEW DATA TO EXISTING DATA
                combined_df = concat([old_data, new_data], ignore_index=True)
                combined_df.to_csv("data.csv", index=False)
            else:
                # PREPARE TO CREATE/WRITE TO NEW FILE
                data = DataFrame(credentials)
                data.to_csv("data.csv", index=False)

            data = read_csv("data.csv")
            print(data)
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
website_label = Label(text="Website", font=("JetBrains Mono", 10, "bold"))
website_label.grid(column=0, row=1)

# WEBSITE ENTRY
website_entry = Entry(relief="groove")
website_entry.grid(column=1, columnspan=2, row=1, sticky="ew")
website_entry.focus()

# EMAIL/USERNAME LABEL
email_user_label = Label(text="Email/Username", font=("JetBrains Mono", 10, "bold"))
email_user_label.grid(column=0, row=2)

# EMAIL/USERNAME ENTRY
email_user_entry = Entry(width=20, relief="groove")
email_user_entry.grid(column=1, columnspan=2, row=2, sticky="ew")
email_user_entry.insert(0, "mikemendez@mail.com")

# PASSWORD LABEL
password_label = Label(text="Password", font=("JetBrains Mono", 10, "bold"))
password_label.grid(column=0, row=3)

# PASSWORD ENTRY
password_entry = Entry(width=20, relief="groove")
password_entry.grid(column=1, row=3, sticky="w")

# GENERATE PASSWORD BUTTON
generate_pwd_button = Button(text="Generate Password", font=("JetBrains Mono", 10, "bold"), command=generate_pwd)
generate_pwd_button.grid(column=2, row=3)

# ADD BUTTON
add_credentials_button = Button(text="Add", font=("JetBrains Mono", 10, "bold"), command=add_credentials)
add_credentials_button.grid(column=1, columnspan=2, row=4, sticky="ew")

window.mainloop()
