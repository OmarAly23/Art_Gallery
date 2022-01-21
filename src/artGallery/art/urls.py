from django.urls import path
from . import views
# from ..artGallery import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('login/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_out/', views.log_out, name='log_out'),
    path('artist/<name>', views.artist, name='artist'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('addToFav/<str:button_id>/', views.addToFav, name='addToFav'),
    path('removeFav/<str:button_id>/', views.removeFav, name='removeFav'),
]