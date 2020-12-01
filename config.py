import os
from os import environ, path
from datetime import timedelta
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DIST_FOLDER = 'dist'
    SERVER_NAME = 'http://localhost:5000'
    STATIC_FOLDER = 'dist/static'
    DEBUG = False
    JSONIFY_MIMETYPE = 'application/json'
    JSONIFY_PRETTYPRINT_REGULAR = False
    JSON_AS_ASCII = True
    JSON_SORT_KEYS = True
    MAX_CONTENT_LENGTH = None
    MAX_COOKIE_SIZE = 4093
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)
    PREFERRED_URL_SCHEME = 'http'
    SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    SESSION_REFRESH_EACH_REQUEST = True
    SQLALCHEMY_BINDS = None
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_ENGINE_OPTIONS = {}
    SQLALCHEMY_MAX_OVERFLOW = None
    SQLALCHEMY_NATIVE_UNICODE = None
    SQLALCHEMY_POOL_RECYCLE = None
    SQLALCHEMY_POOL_SIZE = None
    SQLALCHEMY_POOL_TIMEOUT = None
    SQLALCHEMY_RECORD_QUERIES = None
    TEMPLATES_AUTO_RELOAD = None


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
