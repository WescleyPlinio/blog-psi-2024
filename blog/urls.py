from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('help/', views.help, name="help"),
    path('disturbs/', views.disturbs, name="disturbs"),
    path("post/<int:id>",views.post ,name="post")
]
