from django.db import models


class GameType(models.Model):

    label = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.name
