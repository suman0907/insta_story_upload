from os import environ, path
from information import *





class Config:


    """@staticmethod
    def init_app(WebApp):
        pass"""

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+DB_USER+":"+DB_PASSWORD+'@'+DB_INSTANCE+'/'+DB_DATABASE
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False



