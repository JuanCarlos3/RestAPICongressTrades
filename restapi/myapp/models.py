from django.db import models

class Senator(models.Model):
    Senatorname = models.CharField(max_length=100)
    Tickername = models.CharField(max_length=100)
    number_of_stocks = models.IntegerField()
    date = models.DateField()