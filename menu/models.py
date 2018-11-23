from django.db import models

from helpers import get_image_path


class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500)

    class Meta:
        abstract = True


class Menu(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    dishes = models.ManyToManyField('menu.Dish')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f'{self.name}'


class Dish(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    preparation_time = models.IntegerField()
    is_vegetarian = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    picture = models.ImageField(upload_to=get_image_path, null=True, blank=True, )

    def __str__(self):
        return f'{self.name}, {self.price}'
