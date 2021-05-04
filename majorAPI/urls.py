from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home , name='home'),
    path('screening/', views.screening, name='screening'),
    path('result/', views.result, name='result')
    ]