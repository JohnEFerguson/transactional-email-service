from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    FLASK_ENV = 'development'
    TESTING = True
    MAILGUN_API_KEY = environ.get('MAILGUN_API_KEY')
    SENDGRID_API_KEY = environ.get('SENDGRID_API_KEY')

