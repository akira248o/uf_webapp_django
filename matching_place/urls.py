from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('mri',views.member_register_init,name='mri'),
    path('place_register',views.place_register,name='place_register'),
    
]