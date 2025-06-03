from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('greet/<str:name>', views.greet, name='greet'),
    path('profile/', views.profile, name='profile'),
    
]
