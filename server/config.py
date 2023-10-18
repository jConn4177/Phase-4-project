import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False