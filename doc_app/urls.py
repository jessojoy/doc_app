from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(
        template_name='doctors/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
    ), name='logout'),

    # include app urls (this already brings in /patient/dashboard/)
    path('', include('doc_app_v1.urls')),
]
