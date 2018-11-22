from django.db.models import Count
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import viewsets, mixins

from menu.models import Menu
from menu.serializers import MenuSerializer
from menu.validators import is_valid_order


class MenuListView(ListView):
    model = Menu
    paginate_by = 5
    template_name = 'menu-list.html'

    def get_queryset(self):
        queryset = super(MenuListView, self).get_queryset()

        queryset = queryset.annotate(dishes_count=Count('dishes')).filter(dishes_count__gt=0)

        return queryset

    def get_ordering(self):
        ordering = self.request.GET.get('order_by')

        if ordering and is_valid_order(Menu, ordering, ['dishes_count']):
            return ordering

        return super(MenuListView, self).get_ordering()


class MenuDetailsView(DetailView):
    model = Menu
    template_name = 'menu-details.html'


class MenuDetailsViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
