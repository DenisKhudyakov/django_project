from django.urls import path

from catalog.views import contacts, home


app_name = 'contacts'

urlpatterns = [
    path('', contacts, name='contacts'),
    path('', home, name='home')
]
