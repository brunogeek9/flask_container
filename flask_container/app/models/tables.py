from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(70), unique=True,nullable=False)
    password = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(70), unique=True,nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username