from django.urls import path
from .views import * 
from classroom import views

urlpatterns = [
     path('',views.Home, name="Home"),
     path('graph', views.Graph, name="Graph"),
]
