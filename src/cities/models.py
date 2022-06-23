from django.db import models



class City(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='shahar')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Shahar'
        verbose_name_plural = "Shaharlar"
        ordering = ['name']
