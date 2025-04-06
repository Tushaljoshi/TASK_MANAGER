import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,
        'max_overflow': 20,
        'pool_timeout': 30,
        'pool_recycle': 1800
    }
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/task_db')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

def get_config(name):
    return {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
    }.get(name, DevelopmentConfig)

