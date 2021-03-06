from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index),
    
    path('registro', auth.registro),
    path('login', auth.login),
    path('logout', auth.logout),
    
    path('travels', views.home),
    path('abort/<int:travel_id>', views.abort),
    path('delete/<int:travel_id>', views.delete),
    path('join/<int:travel_id>', views.join),
    
    path('view/<int:travel_id>', views.view),
    
    path('addtrip', views.add)
]
