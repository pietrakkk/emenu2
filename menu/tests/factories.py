import factory


class DishFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Dish {0}'.format(n))
    preparation_time = 20
    description = factory.Sequence(lambda n: 'Description {0}'.format(n))
    price = 30.99
    is_vegetarian = False

    class Meta:
        model = 'menu.Dish'


class MenuFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Menu {0}'.format(n))
    description = factory.Sequence(lambda n: 'Description {0}'.format(n))

    class Meta:
        model = 'menu.Menu'
