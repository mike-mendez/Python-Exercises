import pandas
import tkinter
from os.path import exists


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_credentials():
    if exists("data.csv"):
        data = pandas.read_csv("data.csv")
        # GET NEW CREDENTIALS FROM USER AND ADD TO EXISTING DATA
        credentials = {
            website_label["text"]: website_entry.get(),
            email_user_label["text"]: email_user_entry.get(),
            password_label["text"]: password_entry.get()
        }
    else:
        # PREPARE TO CREATE/WRITE TO NEW FILE
        # data = pandas.DataFrame(credentials)
        # print(credentials)


# ---------------------------- UI SETUP ------------------------------- #

# WINDOW
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# LOGO
logo = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, columnspan=3, row=0)

# WEBSITE LABEL
website_label = tkinter.Label(text="Website", font=("JetBrains Mono", 10, "bold"))
website_label.grid(column=0, row=1)

# WEBSITE ENTRY
website_entry = tkinter.Entry(relief="groove")
website_entry.grid(column=1, columnspan=2, row=1, sticky="ew")
website_entry.focus()

# EMAIL/USERNAME LABEL
email_user_label = tkinter.Label(text="Email/Username", font=("JetBrains Mono", 10, "bold"))
email_user_label.grid(column=0, row=2)

# EMAIL/USERNAME ENTRY
email_user_entry = tkinter.Entry(width=20, relief="groove")
email_user_entry.grid(column=1, columnspan=2, row=2, sticky="ew")
email_user_entry.insert(0, "mikemendez@mail.com")

# PASSWORD LABEL
password_label = tkinter.Label(text="Password", font=("JetBrains Mono", 10, "bold"))
password_label.grid(column=0, row=3)

# PASSWORD ENTRY
password_entry = tkinter.Entry(width=20, relief="groove")
password_entry.grid(column=1, row=3, sticky="w")

# GENERATE PASSWORD BUTTON
generate_pwd_button = tkinter.Button(text="Generate Password", font=("JetBrains Mono", 10, "bold"))
generate_pwd_button.grid(column=2, row=3)

# ADD BUTTON
add_credentials_button = tkinter.Button(text="Add", font=("JetBrains Mono", 10, "bold"), command=add_credentials)
add_credentials_button.grid(column=1, columnspan=2, row=4, sticky="ew")

window.mainloop()
