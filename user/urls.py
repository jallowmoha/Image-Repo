from django.urls import path
from .views import UserView
from django.contrib import admin
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('register/', UserView.as_view(), name="new_user")
]

admin.site.site_header = 'Image Market Place'
admin.site.site_title = 'Image Market Place'