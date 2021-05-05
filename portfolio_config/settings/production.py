from .common import *

ALLOWED_HOSTS = ["eportfolio-mo1.herokuapp.com", "emmanuel-oudot.fr"]

DEBUG = False

# Activate Django-Heroku.
django_heroku.settings(locals())
