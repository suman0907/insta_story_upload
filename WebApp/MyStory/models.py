from sqlalchemy import func
from WebApp import db
import flask_sqlalchemy
from datetime import datetime



class Story_Info(db.Model):
    __tablename__ = 'story_info'
    id =          db.Column(db.Integer,primary_key=True,autoincrement=True)
    grapher_name= db.Column(db.String(64),nullable=False)
    name=         db.Column(db.String(64),nullable=False)
    file=         db.Column(db.LargeBinary)
    description=  db.Column(db.String(255),nullable=False)
    duration =    db.Column(db.Integer)
    type=         db.Column(db.String(64),nullable=False)
    lattitude=    db.Column(db.Float,nullable=False)
    longitude=    db.Column(db.Float,nullable=False)
    timestamp=    db.Column(db.DateTime,server_default=func.now(),nullable=False)


    def import_data(self,data):
        try:
            self.grapher_name= data['grapher_name']
            self.name =       data['name']
            self.description= data['description']
            self.duration=    data.get('duration',None)
            self.type=        data['type']
            self.lattitude=   data['lattitude']
            self.longitude=   data['longitude']
            self.file= data.get('file',None)

            return self

        except Exception as e:
            return str(e)