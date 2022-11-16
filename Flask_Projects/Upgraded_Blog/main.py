from flask import Flask, render_template, request
from requests import get
from smtplib import SMTP

# -------------------------------- CONSTANTS ---------------------------------- #
BLOG_POSTS_URL = "https://api.npoint.io/959fdbf144304c9e47af"
BLOG_POSTS_DATA = get(url=BLOG_POSTS_URL).json()
EMAIL = "[YOUR EMAIL]"
PASSWORD = "[YOUR PASSWORD]"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=BLOG_POSTS_DATA)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def get_contact():
    if request.method == "GET":
        return render_template("contact.html", msg_sent=None)
    else:
        name = f"Name: {request.values['name']}"
        email = f"Email: {request.values['email']}"
        phone = f"{request.values['phone']}"
        message = f"{request.values['message']}"

        # ---------------------- EMAIL MESSAGE -------------------------------- #
        try:
            with SMTP("smtp.gmail.com") as connection:
                connection.starttls()  # Encrypts sent email if read by an interceptor
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs="[RECEIVING EMAIL]",
                    msg=f"Subject: New message\n\n{name}\n{email}\n{phone}\n{message}"
                )
        except:
            return render_template("contact.html", msg_sent=False)
        else:
            return render_template("contact.html", msg_sent=True)


@app.route("/post/<blog_id>")
def get_post(blog_id):
    blog_post = [post for post in BLOG_POSTS_DATA if post["id"] == int(blog_id)]
    return render_template("post.html", post=blog_post[0])


if __name__ == "__main__":
    app.run(debug=True)
