from django.db import models

# Create your models here.

class Sondage(models.Model):
    question = models.CharField(max_length = 200)
    date_publication = models.DateTimeField()

class Response(models.Model):
    sondage = models.ForeignKey(Sondage)
    nb_votes = models.IntegerField()
