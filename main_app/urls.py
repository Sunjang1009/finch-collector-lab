from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('corgis/', views.CorgisList.as_view(), name="corgis_list"),
]




