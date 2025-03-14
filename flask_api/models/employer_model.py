from sqlalchemy_utils import ChoiceType
from flask_api import db


class employer_model(db.Model):
    """
    Employer model.
    """

    __tablename__ = 'employers'

    gender_choice = [('M', 'Masculino'), ('F', 'Feminino')]

    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(ChoiceType(gender_choice), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    cpf = db.Column(db.String(50), unique=True, nullable=False)
    enterprise = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(50), nullable=False)
