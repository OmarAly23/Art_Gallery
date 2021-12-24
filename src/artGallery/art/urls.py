from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^index2$', views.index2, name='index2'),
]