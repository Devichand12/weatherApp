from django.db import models

# Create your models here.
class Weather(models.Model):
    city=models.CharField(max_length=20)
    temperature=models.CharField(max_length=10)

    def __str__(self):
        return self.city
