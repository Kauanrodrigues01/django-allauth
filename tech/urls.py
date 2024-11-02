from django.contrib import admin
from django.urls import path
from .views import index, members

urlpatterns = [
    path('', index, name='home'),
    path('members/', members, name='page-memebers')
]
