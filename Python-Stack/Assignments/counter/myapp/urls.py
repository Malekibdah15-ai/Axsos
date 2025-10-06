from django.contrib import admin
from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),    
    path('destroy_sessio', views.destroy_session),
    path('admin/', admin.site.urls),
    
      
]