from mhoapp.settings.common import *
import django_heroku

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']

django_heroku.settings(locals())