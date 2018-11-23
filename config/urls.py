from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from config import settings
from menu.views import MenuDetailsViewSet, MenuListView, MenuDetailsView

router = routers.DefaultRouter()

router.register(r'menu', MenuDetailsViewSet, base_name='menu')

urlpatterns = [
    url(r'api/', include(router.urls)),
    path('', MenuListView.as_view(), name='menu-list'),
    path('<int:pk>/', MenuDetailsView.as_view(), name='menu-detail-view'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL)
