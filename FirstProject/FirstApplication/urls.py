from django.urls import path
from . import views

urlpatterns = [
    path('i/', views.index, name='index'),
    path('a/', views.about, name='about'),
    path('w/', views.welcome, name='welcome'),
    path('c/', views.login, name='model_entry'),
]
