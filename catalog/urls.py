from django.urls import path

from catalog.views import ContactsView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, VersionCreateView, \
    VersionUpdateView, VersionDetailView


from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('card/<int:pk>/', ProductDetailView.as_view(), name='card'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('prouct/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('version/', VersionCreateView.as_view(), name='version_create'),
    path('version/<int:pk>/update/', VersionUpdateView.as_view(), name='version_update'),
    path('version/<int:pk>', VersionDetailView.as_view(), name='version_detail')
]
