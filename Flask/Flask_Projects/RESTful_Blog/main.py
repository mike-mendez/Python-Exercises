from flask import Flask, jsonify, redirect, render_template, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def home():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.get(index)
    return render_template("post.html", post=requested_post)


@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    blog_form = CreatePostForm()
    if blog_form.validate_on_submit():
        new_blog = BlogPost(
            title=request.form.get("title"),
            subtitle=request.form.get("subtitle"),
            author=request.form.get("author"),
            img_url=request.form.get("img_url"),
            body=request.form.get("body"),
            date=datetime.now().strftime("%B %d, %Y"),
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("make_post.html", form=blog_form)


@app.route("/add_post", methods=["POST"])
def add_post():
    blog_form = CreatePostForm()
    return render_template("make_post.html", form=blog_form)


@app.route("/edit_post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(obj=post)
    if edit_form.validate_on_submit():
        edit_form.populate_obj(post)
        db.session.commit()
        return redirect(url_for("show_post", index=post_id))
    return render_template("make_post.html", form=edit_form)


@app.route("/delete_post/<int:post_id>")
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
