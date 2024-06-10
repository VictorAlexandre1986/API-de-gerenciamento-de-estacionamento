import flaskr.config_app as ca
from flaskr.db import db_instance, db_persist


class RentModel(db_instance.Model):
    __tablename__ = 'alugueis'


    id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)
    username = db_instance.Column(db_instance.String(80), db_instance.ForeignKey('users.username'), nullable=False)
    name = db_instance.Column(db_instance.String(80))
    plate = db_instance.Column(db_instance.String(10))
    model = db_instance.Column(db_instance.String(80))
    rent_date_initial = db_instance.Column(db_instance.DateTime)
    rent_date_final = db_instance.Column(db_instance.DateTime)
    total = db_instance.Column(db_instance.Integer)


    def __init__(self, username, name, plate, model, rent_date_initial, rent_date_final=None,total=0, id=None):
        self.username = username
        self.name = name
        self.plate = plate
        self.model = model
        self.rent_date_initial = rent_date_initial
        self.rent_date_final = rent_date_final
        self.total= total

        
    
    def __repr__(self):
        return "<RentModel(id={self.id!r}, username={self.username!r})> , plate={self.plate!r}, rent_date_initial={self.rent_date_initial}, rent_date_final={rent_date_final}".format(self=self)

    @db_persist
    def save(self):
        db_instance.session.add(self)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_plate(cls, _plate):
        return cls.query.filter_by(plate=_plate).first()
    
    @classmethod
    def find_by_date(cls, _rent_date_initial):
        return cls.query.filter_by(rent_date_initial=_rent_date_initial).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @db_persist
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db_instance.session.commit()

    @classmethod
    @db_persist
    def delete_by_id(cls, _id):
        instance = cls.find_by_id(_id)
        if instance:
            db_instance.session.delete(instance)
            db_instance.session.commit()
            return True
        return False

    @staticmethod
    def init_data():
        if db_instance.session.query(RentModel.id).count() == 0:
            for count_rent in range(1, 6):
                rent = RentModel(username="user" + str(count_rent), name="name" + str(count_rent), plate="plate" + str(count_rent), model="model" + str(count_rent), rent_date_initial="rend_date_initial" + str(count_rent), rent_date_final="rent_date_final" + str(count_rent))
                rent.save()


