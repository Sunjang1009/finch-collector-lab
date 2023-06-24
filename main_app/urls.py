from django.urls import path
from . import views

urlpatterns = [
    # views.py for a class that is named home at localhost 8001/
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('corgis/', views.CorgisList.as_view(), name="corgis_list"),
    path('corgis/new/', views.CorgiCreate.as_view(), name="corgi_create"),
]






