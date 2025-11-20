# doc_app/urls.py  — paste this exact file (replace existing)
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Global login/logout so the name 'login' exists site-wide
    path('login/', auth_views.LoginView.as_view(template_name='doctors/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # Now include your app urls
    # IMPORTANT: change 'doc_app_v1' below if your app package name differs
    path('', include('doc_app_v1.urls')),
]
