#import os


class Config:
    SECRET_KEY = '05db826f11ce507332264d30bfb42608'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.{youremailhost}.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = '{youremail}@{youremailhost}.com'
    MAIL_PASSWORD = '{yourpassword}'
    
