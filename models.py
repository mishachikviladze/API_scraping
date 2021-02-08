'''Docstring ...'''
from db import db

class MyhomeFlatsAppartments_model(db.Model):
    __tablename__ = 'MyhomeFlatsAppartments'

    ID = db.Column(db.Integer, primary_key=True)
    APP_ID = db.Column(db.Integer)
    statement_date = db.Column(db.String(10))
    owner = db.Column(db.String(300))
    owner_type = db.Column(db.String(50))
    statements_count = db.Column(db.String(50))
    owner_statements = db.Column(db.String(50))
    current_staytement_url = db.Column(db.String(300))
    address = db.Column(db.String(300))
    amount_GEL = db.Column(db.Float(precision=2))
    amount_USD = db.Column(db.Float(precision=2))
    badrooms = db.Column(db.String(50))
    floor = db.Column(db.String(50))
    other_characteristics = db.Column(db.String(300))
    phone = db.Column(db.String(50))
    rooms = db.Column(db.String(50))
    square = db.Column(db.String(50))
    insertDate = db.Column(db.String(10))

    def __init__(self, ID, APP_ID, statement_date, owner, owner_type, statements_count, owner_statements, current_staytement_url, address, amount_GEL, amount_USD, badrooms, floor, other_characteristics, phone, rooms, square, insertDate):
        self.ID = ID
        self.APP_ID = APP_ID
        self.statement_date = statement_date
        self.owner = owner
        self.owner_type = owner_type
        self.statements_count = statements_count
        self.owner_statements = owner_statements
        self.current_staytement_url = current_staytement_url
        self.address = address
        self.amount_GEL = amount_GEL
        self.amount_USD = amount_USD
        self.badrooms = badrooms
        self.floor = floor
        self.other_characteristics = other_characteristics
        self.phone = phone
        self.rooms = rooms
        self.square = square
        self.insertDate = insertDate

    def json(self):
        return {
            'ID': self.ID,
            'APP_ID':self.APP_ID,
            'statement_date':self.statement_date.__str__(),
            'owner':self.owner,
            'owner_type':self.owner_type,
            'statements_count':self.statements_count,
            'owner_statements':self.owner_statements,
            'current_staytement_url':self.current_staytement_url,
            'address':self.address,
            'amount_GEL':self.amount_GEL,
            'amount_USD':self.amount_USD,
            'badrooms':self.badrooms,
            'floor':self.floor,
            'other_characteristics':self.other_characteristics,
            'phone':self.phone,
            'rooms':self.rooms,
            'square':self.square,
            'insertDate':self.insertDate.__str__()
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()
