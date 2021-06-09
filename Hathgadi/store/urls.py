from django.contrib import admin
from django.urls import path
from .views import store, Vendors,Signup,Login,logout
urlpatterns = [
    path('', store, name='storepage'),
    path('<int:items_id>', Vendors, name = 'vendorpage'),
    path('signup', Signup.as_view(), name="signup"),
    path('login',  Login.as_view(),  name="login"),
    path('logout', logout,  name="logout"),
]