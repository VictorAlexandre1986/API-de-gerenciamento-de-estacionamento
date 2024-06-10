import flaskr.config_app as ca
from flaskr.db import db_instance, db_persist


class UserModel(db_instance.Model):
    __tablename__ = 'users'


    id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)
    username = db_instance.Column(db_instance.String(80))
    password = db_instance.Column(db_instance.String(80))

    def __init__(self, username, password, id=None):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return "<UserModel(id={self.id!r}, username={self.username!r})>".format(self=self)

    @db_persist
    def save(self):
        db_instance.session.add(self)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @staticmethod
    def init_data():
        if db_instance.session.query(UserModel.id).count() == 0:
            for count_user in range(1, 6):
                user = UserModel(username="user" + str(count_user), password="pwd" + str(count_user))
                user.save()


