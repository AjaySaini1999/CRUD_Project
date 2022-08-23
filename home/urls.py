"""crudproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from home import views
from .views import Edit_stu
urlpatterns = [
    path('', views.index, name='home'),
    path('add_stu', views.add_stu, name='add_stu'),
    path('del_stu', views.del_stu, name='del_stu'),
    path('edit_stu/<int:id>/', Edit_stu.as_view(), name='edit_stu'),



]
