from django.urls import path
from . import views
# from ..artGallery import settings

urlpatterns = [
    path('', views.index, name='index'),
    # path(r'^index2$', views.index2, name='index2'),
]