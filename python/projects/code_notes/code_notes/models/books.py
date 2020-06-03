from datetime import datetime
from code_notes import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)

    def __repr__(self):
        return f"Book('{self.title} {self.author_id}')"


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    books = db.relationship("Book", backref="author", lazy=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    surname = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Author('{self.name} {self.surname}')"
