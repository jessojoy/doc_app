from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage/', views.homepage, name='homepage_with_slash'),
    path('register/', views.register, name='register'),
]
