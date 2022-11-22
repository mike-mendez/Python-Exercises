from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,"
#                "title varchar(250) NOT NULL UNIQUE,"
#                "author varchar(250) NOT NULL,"
#                "rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()
    new_book = Books(title="Harry Potter", author="J. K. Rowling", rating=9.3, )
    db.session.add(new_book)
    db.session.commit()

