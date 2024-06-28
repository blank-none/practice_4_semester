import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:mersedesVD@localhost/encryption_service')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
