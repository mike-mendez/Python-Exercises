from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


@app.route('/')
def home():
    with app.app_context():
        db.create_all()
    all_books = Books.query.all()
    return render_template("index.html", books=all_books)


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    with app.app_context():
        new_book = Books(title=request.values["title"],
                         author=request.values["author"],
                         rating=request.values["rating"])
        db.session.add(new_book)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<id>")
def delete(id):
    with app.app_context():
        book_to_delete = Books.query.get(id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/edit_rating/<id>")
def edit_rating(id):
    with app.app_context():
        book_to_update = Books.query.get(id)
    return render_template("edit_rating.html", book=book_to_update)


@app.route("/change_rating/<id>", methods=["GET", "POST"])
def change_rating(id):
    with app.app_context():
        book_to_update = Books.query.get(id)
        book_to_update.rating = request.values["new_rating"]
        db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
