from django.urls import path
from . import views

urlpatterns = [
    path('', views.GPT, name='GPT'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
]