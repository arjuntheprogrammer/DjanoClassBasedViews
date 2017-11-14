from django.conf.urls import include, url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^about-us/$', views.AboutUsView.as_view(), name= 'about_us'),
]
