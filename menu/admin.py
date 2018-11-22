from django import forms
from django.contrib import admin

from menu.models import Menu, Dish


class DishModelForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    preparation_time = forms.IntegerField(min_value=1)
    price = forms.DecimalField(min_value=0)

    class Meta:
        fields = ('name', 'description', 'preparation_time', 'price', 'is_vegetarian',)
        model = Dish


class MenuAdmin(admin.ModelAdmin):
    model = Menu
    fields = ('name', 'description', 'dishes',)
    filter_horizontal = ('dishes',)
    list_display = ('name', 'creation_date',)


class DishAdmin(admin.ModelAdmin):
    form = DishModelForm
    model = Dish
    list_display = ('name', 'creation_date', 'modification_date', 'price_',)

    def price_(self, obj):
        return f'{obj.price} PLN'


admin.site.register(Menu, MenuAdmin)
admin.site.register(Dish, DishAdmin)
