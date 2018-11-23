from django.db import models

from helpers import get_image_path


class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    description = models.CharField('Opis', max_length=500)

    class Meta:
        abstract = True


class Menu(BaseModel):
    name = models.CharField('Nazwa', max_length=200, unique=True)
    dishes = models.ManyToManyField('menu.Dish', verbose_name='Potrawy')

    class Meta:
        verbose_name_plural = 'Karty menu'
        ordering = ('id',)


def __str__(self):
    return f'{self.name}'


class Dish(BaseModel):
    name = models.CharField('Nazwa', max_length=200, unique=True)
    preparation_time = models.IntegerField('Czas przygotowania')
    is_vegetarian = models.BooleanField('Potrawa wegetariańska?', default=False)
    price = models.DecimalField('Cena', decimal_places=2, max_digits=5)
    picture = models.ImageField('Obrazek', upload_to=get_image_path, null=True, blank=True, )

    class Meta:
        verbose_name = 'Potrawa'
        verbose_name_plural = 'Potrawy'

    def __str__(self):
        return f'{self.name}, {self.price}'
