from django.db import models
from django.core.exceptions import ValidationError

from cities.models import City

class Train(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Poyezd nomi'
        )
    travel_time = models.PositiveSmallIntegerField(verbose_name="Yo'l vaqti")
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='from_city_set',
        verbose_name='Qaysi shahardan'
        )
    to_city = models.ForeignKey(
        'cities.City',
        on_delete=models.CASCADE,
        related_name='to_city_set',
        verbose_name='Qaysi shaharga'
        )


    def __str__(self):
        return f"{self.from_city} shahridan {self.to_city} shahriga {self.name} poyezdi"

    class Meta:
        verbose_name = "Poyezd"
        verbose_name_plural = "Poyezdlar"
        ordering = ['travel_time']


    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError("Shaharlardan birini o'zgartiring!")
        qs = Train.objects.filter(
            from_city=self.from_city,
            to_city=self.to_city,
            travel_time=self.travel_time
        ).exclude(pk=self.pk)
        # Train == self.__class__
        if qs.exists():
            raise ValidationError("Yo'l vaqtini o'zgartiring!")

    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)