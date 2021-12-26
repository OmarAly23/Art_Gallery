from django.urls import path
from . import views
# from ..artGallery import settings

urlpatterns = [
    path('', views.index, name='index'),
    # path('signup/', views.signup_view, name='signup'),
]