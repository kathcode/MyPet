from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    type = models.IntegerField()

    def __str__(self):
        return self.name
