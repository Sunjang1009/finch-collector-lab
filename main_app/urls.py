from django.urls import path
from . import views

urlpatterns = [
    # views.py for a class that is named home at localhost 8001/
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('corgis/', views.CorgisList.as_view(), name="corgis_list"),
    path('corgis/<int:pk>/', views.CorgiDetail.as_view(), name="corgi_detail"),
    path('corgis/new/', views.CorgiCreate.as_view(), name="corgi_create"),
    path('corgis/<int:pk>/update/', views.CorgiUpdate.as_view(), name="corgi_update"),
    path('corgis/<int:pk>/delete/', views.CorgiDelete.as_view(), name="corgi_delete"),
    path('corgis/<int:pk>/dogs/new/', views.DogCreate.as_view(), name="dog_create"),
    path('doglists/<int:pk>/dogs/<int:dog_pk>', views.DoglistDogAssoc.as_view(), name="doglist_dog_assoc"),
]














