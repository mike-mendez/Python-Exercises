from smtplib import SMTP

email = "sending_email@gmail.com"
password = "password"
with SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # Encrypts sent email if read by an interceptor
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs="receiving_email@gmail.com",
        msg="Subject:This Message Was Sent Using Python!\n\nPython!!!"
    )
