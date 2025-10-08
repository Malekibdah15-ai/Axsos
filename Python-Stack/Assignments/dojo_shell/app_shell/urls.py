from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index),
    path('creating/dojos', views.create_Dojo),
    path('create/ninjas', views.create_ninja),
    
    
]
