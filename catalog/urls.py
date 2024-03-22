from django.urls import path

from catalog.views import contacts, basket
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', basket, name='basket'),
    path('contacts/', contacts, name='contacts'),
]
