from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage/', views.homepage, name='homepage_with_slash'),
    path('register/', views.register, name='register'),

    # Patient dashboard route (note views.)
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
]
