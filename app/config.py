# Jack Ferguson 2021
# ideally all of this config would be taken from a yml file or env vars
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

ENV = 'development'
TESTING = False 
## make this more robust
USE_MAILGUN = environ.get('API_TO_USE') == 'mailgun'
MAILGUN_API_KEY = environ.get('MAILGUN_API_KEY')
SENDGRID_API_KEY = environ.get('SENDGRID_API_KEY')

