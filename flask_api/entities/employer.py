"""Employer entity module."""


class employer:
    """
    Employer class.
    """

    def __init__(
        self, name, gender, birth_date, cpf, enterprise, role, email, phone
    ):
        self.__name = name
        self.__gender = gender
        self.__birth_date = birth_date
        self.__cpf = cpf
        self.__enterprise = enterprise
        self.__role = role
        self.__email = email
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self.__birth_date = birth_date

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def enterprise(self):
        return self.__enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        self.__enterprise = enterprise

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone
