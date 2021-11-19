from django.db import models

class DeniedWordsManager(models.Manager):

    def in_email(self):
        return DeniedWordsInEmail.objects.all()

    def in_message(self):
        return DeniedWordsInMessage.objects.all()

class DeniedWordsInEmail(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word

class DeniedWordsInMessage(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word
