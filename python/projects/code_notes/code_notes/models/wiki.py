from datetime import datetime
from code_notes import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_edited = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # TODO: edition history?
    content = db.Column(db.Text, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    modified_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    modified_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    tags = db.relationship("Tag", backref="name", lazy=True)
    # private = db.Column(db.Boolean, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    notes = db.relationship("Note", backref="title", lazy=True)

    def __repr__(self):
        return f"Tag('{self.name}')"
