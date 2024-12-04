from django.urls import path

from . import views

app_name = 'app_ia'

urlpatterns = [
    path('',views.index),
    path('recommend/', views.recommend, name='recommend'),
]

