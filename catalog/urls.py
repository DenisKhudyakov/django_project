from django.urls import path

from catalog.views import ContactsView, ProductListView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('card/<int:pk>/', ProductDetailView.as_view(), name='card'),

]
