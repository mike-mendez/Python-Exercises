from flask import Flask, render_template
from requests import get

blog_posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_posts_data = get(url=blog_posts_url).json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts_data)


@app.route("/post/<blog_id>")
def get_post(blog_id):
    blog_post = [post for post in blog_posts_data if post["id"] == int(blog_id)]
    return render_template("post.html", post=blog_post[0])


if __name__ == "__main__":
    app.run(debug=True)
