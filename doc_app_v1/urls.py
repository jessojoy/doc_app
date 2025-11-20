from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage/', views.homepage, name='homepage_with_slash'),

    path('admin-login/', views.admin_login, name="admin_login"),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Manage doctors list page
    path("admin-doctors/", views.manage_doctors, name="manage_doctors"),

    # CRUD for doctor
    path("admin-doctor/add/", views.add_doctor, name="add_doctor"),
    path("admin-doctor/<int:id>/edit/", views.edit_doctor, name="edit_doctor"),
    path("admin-doctor/<int:id>/view/", views.view_doctor, name="view_doctor"),
    path("admin-doctor/<int:id>/delete/", views.delete_doctor, name="delete_doctor"),
    path("admin-patients/", views.view_patients, name="view_patients"),
    path("admin-patient/<str:id>/details/", views.patient_details, name="patient_details"),
    path("admin-appointments/", views.view_appointments, name="view_appointments"),
    path("admin-feedback/", views.view_feedback, name="view_feedback"),

]
