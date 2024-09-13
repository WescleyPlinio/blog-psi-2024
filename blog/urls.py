from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('help.html', views.help, name="help"),
    path('disturbs.html', views.disturbs, name="disturbs"),
    path('aboutus.html', views.aboutus, name="aboutus")
]
