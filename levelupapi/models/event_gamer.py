
from django.db import models
from .gamer import Gamer
from .events import Event



class EventGamer(models.Model):
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
