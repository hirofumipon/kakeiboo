"""
URL configuration for kakeiboo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from kakeiboo_app.views import toppage_view
from kakeiboo_app.views import dashboard_view
from kakeiboo_app.views import input_view
from kakeiboo_app.views import graph_view
from kakeiboo_app.views import settings_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('toppage/', toppage_view, name='toppage'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('input/', input_view, name='input'),
    path('graph/', graph_view, name='graph'),
    path('settings/', settings_view, name='settings')
]
