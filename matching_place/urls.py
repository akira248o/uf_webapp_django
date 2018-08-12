from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('member_register',views.member_register,name='member_register'),
    path('place_register',views.place_register,name='place_register'),
    
]