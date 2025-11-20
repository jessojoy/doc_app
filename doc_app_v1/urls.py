from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('', views.homepage, name='homepage'),      # root (/)
    path('homepage/', views.homepage, name='homepage_with_slash'),  # optional
]
