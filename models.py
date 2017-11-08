from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return self.name

class Station(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'stations'

    id = db.Column(db.Integer, primary_key = True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

class Forward(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'forward'

    id = db.Column(db.BIGINT, primary_key = True)
    fwd = db.Column(db.BIGINT)

    def __init__(self, src, fwd):
        self.id = src
        self.fwd = fwd

class Source(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'source'

    src = db.Column(db.BIGINT, primary_key = True)
    dst = db.Column(db.BIGINT)
    text = db.Column(db.TEXT)

    def __init__(self, src, dst, text):
        self.src = src
        self.dst = dst
        self.text = text

