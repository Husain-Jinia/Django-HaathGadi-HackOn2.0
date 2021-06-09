from django.contrib import admin
from django.urls import path
from .views import store, Vendors
urlpatterns = [
    path('', store, name='storepage'),
    path('<int:items_id>', Vendors, name = 'vendorpage')
]