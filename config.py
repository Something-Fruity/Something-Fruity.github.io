"""Holds configuration class for the application"""
import os
from tempfile import mkdtemp
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:   # pylint: disable=too-few-public-methods
    """Base config."""
    FLASK_APP = os.environ.get('FLASK_APP')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TEMPLATES_AUTO_RELOAD = True
    BABEL_DEFAULT_LOCALE = 'en'
    LANGUAGES = ['en', 'fr']

    SESSION_FILE_DIR = mkdtemp()
    SESSION_PERMANENT = True
    SESSION_TYPE = "filesystem"
    SESSION_COOKIE_PATH = "/"

    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_DB = os.environ.get('MYSQL_DB')

class ProdConfig(Config):   # pylint: disable=too-few-public-methods
    """Additional settings for production environment"""
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')


class DevConfig(Config):   # pylint: disable=too-few-public-methods
    """Additional settings for development environment"""
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')


class TestConfig(Config):   # pylint: disable=too-few-public-methods
    """Additional settings for test environment"""
    FLASK_ENV = 'testing'
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    DATABASE_URI = 'sqlite:///:memory:'  # use a temporary in memory database for testing purposes
