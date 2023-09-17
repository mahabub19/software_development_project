from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contact/',views.contact,name='contact'),
    path('cv/',views.cv,name='cv'),
    path('contact_info/',views.contact_info,name='contact_info'),
    path('image/<str:pk>/',views.image,name='see_image'),
]
