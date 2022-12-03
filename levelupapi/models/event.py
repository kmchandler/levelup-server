from django.db import models
from .gamer import Gamer
from .game import Game

class Event(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
