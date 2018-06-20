import os
import json
from lapdance.core import db
from datetime import datetime
from binascii import hexlify


def to_json(data):
    data.pop('_sa_instance_state')
    return json.dumps(data, indent=4, separators=(',', ': '))


class APIKey(db.Model):
    __tablename__ = 'api_key'

    key = db.Column(db.String, primary_key=True, default=hexlify(os.urandom(32)).decode())
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    created_by = db.Column(db.String)
    description = db.Column(db.String)
    enabled = db.Column(db.Boolean, default=True)

    @classmethod
    def add(cls, data):
        new_key = cls(**data)
        db.session.add(new_key)
        db.session.commit()

        return new_key

    @classmethod
    def get_one(cls, key, as_json=False):
        result = cls.query.filter(
            cls.key == key,
        )

        if as_json:
            data = result.one()
            data.created_at = data.created_at.strftime('%Y-%m-%d %H:%M:%S')
            return to_json(data.__dict__) if as_json else data

        return result.one_or_none()

    @classmethod
    def get_many(cls):
        return cls.query.all()

    @classmethod
    def delete(cls, key):
        deleted = db.session.query(APIKey).filter(cls.key == key).one()
        db.session.delete(deleted)
        db.session.commit()
