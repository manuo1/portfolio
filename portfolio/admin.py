from django.contrib import admin

from .models import (
    DeniedWordsInEmail,
    DeniedWordsInMessage,
)

""" add models to admin page """

admin.site.register(DeniedWordsInEmail)
admin.site.register(DeniedWordsInMessage)
