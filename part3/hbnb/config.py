"""Configuration settings for the HBnB application."""
import os


class Config:
    """Base configuration class."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///production.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
