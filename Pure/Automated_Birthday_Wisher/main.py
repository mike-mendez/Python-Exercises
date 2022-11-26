from datetime import datetime
from os import walk
from pandas import read_csv
from random import randrange
from smtplib import SMTP

# ----------------------------- CONSTANTS --------------------------------------- #
EMAIL = "sending@gmail.com"
PASSWORD = "password"  # mail
CURRENT_MONTH = datetime.now().month
CURRENT_DAY = datetime.now().day

# ------------------------------- GLOBALS --------------------------------------- #
birthdays_today = []
letter_count = 0

# --------------------------- DATA RETRIEVAL ------------------------------------ #
birthdays = read_csv("birthdays.csv").to_dict(orient="records")
for birthday in birthdays:
    if birthday["month"] == CURRENT_MONTH and birthday["day"] == CURRENT_DAY:
        birthdays_today.append(birthday)

if len(birthdays_today) == 0:
    print("No one on in your list has a birthday today.")
else:
    # ---------------------------- LETTER COUNT ------------------------------------ #
    try:
        for root_dir, cur_dir, files in walk(r'./letter_templates'):
            letter_count += len(files)
    except:
        print("You have no letters to send.")
    else:
        # ---------------------------- BIRTHDAY LOOP ----------------------------------- #
        for birthday in birthdays_today:
            # ------------------------ FORMAT LETTER ----------------------------------- #
            try:
                with open(f"letter_templates/letter_{randrange(letter_count)}.txt") as letter:
                    chosen_letter = letter.read()
            except:
                pass
            else:
                formatted_letter = chosen_letter.replace("[NAME]", f"{birthday['name']}")
                # ----------------------- EMAIL LETTER ------------------------------------ #
                try:
                    with SMTP("smtp.gmail.com") as connection:
                        connection.starttls()  # Encrypts sent email if read by an interceptor
                        connection.login(user=EMAIL, password=PASSWORD)
                        connection.sendmail(
                            from_addr=EMAIL,
                            to_addrs=f"{birthday['email']}",
                            msg=f"Subject: Happy Birthday {birthday['name']}\n\n{formatted_letter}"
                        )
                except:
                    print("Unable to send email")
