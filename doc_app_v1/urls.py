from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage/', views.homepage, name='homepage_with_slash'),

    # Admin login + dashboard
    path('admin-login/', views.admin_login, name="admin_login"),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path("admin-logout/", views.admin_logout, name="admin_logout"),


    # Doctors
    path("admin-doctors/", views.manage_doctors, name="manage_doctors"),
    path("admin-doctor/add/", views.add_doctor, name="add_doctor"),
    path("admin-doctor/<int:id>/edit/", views.edit_doctor, name="edit_doctor"),
    path("admin-doctor/<int:id>/view/", views.view_doctor, name="view_doctor"),
    path("admin-doctor/<int:id>/delete/", views.delete_doctor, name="delete_doctor"),

    # Patients
    path("admin-patients/", views.view_patients, name="view_patients"),
    path("admin-patient/<str:id>/details/", views.patient_details, name="patient_details"),

    # Appointments
    path("admin-appointments/", views.view_appointments, name="view_appointments"),


     # PATIENT URLS
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('patient/profile/', views.patient_profile, name='patient_profile'),
    path('patient/book-appointment/', views.book_appointment, name='book_appointment'),




    # Feedback
    path("admin-feedback/", views.view_feedback, name="view_feedback"),


    # Register
    path("register/", views.register, name="register"),
]
