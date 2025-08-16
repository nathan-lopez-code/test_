from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom du fruit')
    description = models.TextField(verbose_name='Description du fruit', blank=True, null=True)
    image = models.ImageField(verbose_name='Image du fruit', blank=True, null=True, upload_to='media/fruits')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.upper()