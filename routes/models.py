from django.db import models
from django.core.exceptions import ValidationError

from cities.models import City



class Route(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Marshrut nomi"
        )
    travel_times = models.PositiveSmallIntegerField(verbose_name="Umumiy yo'l vaqti")
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='route_from_city_set',
        verbose_name='Qaysi shahardan'
        )
    to_city = models.ForeignKey(
        'cities.City',
        on_delete=models.CASCADE,
        related_name='route_to_city_set',
        verbose_name='Qaysi shaharga'
        )
    
    trains = models.ManyToManyField('trains.Train', verbose_name="Poyezdlar ro'yhati")


    def __str__(self):
        return f"{self.from_city} shahridan {self.to_city} shahriga {self.name} marshruti"

    class Meta:
        verbose_name = "Marshrut"
        verbose_name_plural = "Marshrutlar"
        ordering = ['travel_times']
