from django.urls import path
from . import views
# from ..artGallery import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout, name='logout'),
    # path('testcookie/', views.cookie_session),
    # path('deletecookie/', views.cookie_delete),
    # path('create/', views.create_session),
    # path('access/', views.access_session),
]