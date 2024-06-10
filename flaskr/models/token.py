import flaskr.config_app as ca
from flaskr.db import db_instance, db_persist


class TokenBlocklistModel(db_instance.Model):
    __tablename__ = 'token_block_list'


    id = db_instance.Column(db_instance.Integer, primary_key=True)
    jti = db_instance.Column(db_instance.String(36), nullable=False, index=True)
    created_at = db_instance.Column(db_instance.DateTime, nullable=False)

    @classmethod
    def get_token(cls, jti):
        return db_instance.session.query(TokenBlocklistModel.id).filter_by(jti=jti).scalar()

    @db_persist
    def save(self):
        db_instance.session.add(self)


