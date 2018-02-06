from . import views
from django.urls import path

app_name = 'dukapp'
urlpatterns = [
    path('', views.home, name='index'),
]