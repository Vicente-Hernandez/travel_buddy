from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index),
    path('registro', auth.registro),
    path('login', auth.login),
    path('logout', auth.logout),
    path('home', views.home),
    #path('travels', views.travels),
    #path('travels/add', views.travels_add),
    #path('join/<id>', views.join),
    #path('travels/destination/<id>', views.travels_id),
    #path('delete/<id>', views.delete_id),
    #path('cancel/<id>', views.cancel_id)
]
