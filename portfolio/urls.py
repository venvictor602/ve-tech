from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('Our_Works/', views.ourwork, name = 'our_work'),
    path('contact_us', views.contact, name = 'contact'),
]