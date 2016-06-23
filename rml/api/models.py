from django.db import models

# Create your models here.

class Data(models.Model):
    date = models.TextField()
    time = models.TextField()
    message = models.TextField()

    