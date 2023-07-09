from app import db

class Task(db.Model):
    id = db.Column(db.String, primary_key=True)
    image_name = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=True)