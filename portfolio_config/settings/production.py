from .common import *

import django_heroku

ALLOWED_HOSTS = ["eportfolio-mo1.herokuapp.com", "emmanuel-oudot.fr"]

DEBUG = False

# Activate Django-Heroku.
django_heroku.settings(locals())
