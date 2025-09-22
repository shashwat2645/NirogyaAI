from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('login', views.loginUser, name="login"),
    path('test', views.test, name="test"),
    path('health', views.health, name="health"),
]
    # path('register', views.register, name="register"),
