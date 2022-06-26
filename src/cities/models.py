from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=128, unique=True,)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Shahar'
        verbose_name_plural = "Shaharlar"
        ordering = ['name']

    
    def get_absolute_url(self):
        return reverse("cities:detail_city", kwargs={"pk": self.pk})
    
