from app import db

class User(db.model):
    __tablename__ = "users"

    id = db.column(db.Integer, primary_key=true)
    username = db.column(db.String(70), unique=True)
    password = db.column(db.String(100))
    email = db.column(db.String(70), unique=True)