from django.urls import path

from catalog.views import ContactsView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, VersionCreateView


from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('card/<int:pk>/', ProductDetailView.as_view(), name='card'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('prouct/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('version/<int:pk>/', VersionCreateView.as_view(), name='version_create'),
]
