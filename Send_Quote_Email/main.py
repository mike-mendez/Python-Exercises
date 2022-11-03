from datetime import datetime
from random import choice
from smtplib import SMTP

EMAIL = "sending@gmail.com"
PASSWORD = "password"  # mail
current_day = datetime.now().weekday()
if current_day == 3:
    with open("quotes.txt") as quotes:
        q_o_d = choice(quotes.readlines())
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Encrypts sent email if read by an interceptor
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="receiving@gmail.com",
            msg=f"Subject:Here's Your Quote of the Day\n\n{q_o_d}"
        )
