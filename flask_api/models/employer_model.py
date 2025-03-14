from flask_api import db


class EmployerModel(db.Model):
    """
    Employer model.
    """

    __tablename__ = 'employers'

    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    cpf = db.Column(db.String(50), unique=True, nullable=False)
    enterprise = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(50), nullable=False)
