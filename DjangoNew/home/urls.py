from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name="home"),
    path('downloads',views.downloads,name="downloads"),
    path('contact',views.contact,name="contact"),
    path('login', views.loginuser,name="login"),
    path('logout', views.logoutuser,name="logout"),
    path('signin',views.signin,name='signin'),
]