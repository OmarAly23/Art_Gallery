from django.urls import path
from . import views
# from ..artGallery import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.sign_in, name='sign_in'),
    path('signup', views.sign_up, name='sign_up')
    # path('signup/', views.signup_view, name='signup'),
]