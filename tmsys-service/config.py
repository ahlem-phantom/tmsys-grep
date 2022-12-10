import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Development environment configuration
    """
    ENV = "development"
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    """
    Production environment configurations
    """
    ENV = "production"
    uri = os.environ['DATABASE_URL']
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = uri
    SECRET_KEY = os.environ['SECRET_KEY']
