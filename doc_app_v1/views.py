from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login



# Create your views here.
def homepage(request):
    return render(request,'doctors/homepage.html')

  
def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("admin_dashboard")
        else:
            return render(request, "admin/admin_login.html", {"error": "Invalid login details"})

    return render(request, "admin/admin_login.html")
  
def admin_dashboard(request):

    context = {
        "total_doctors": 48,
        "total_patients": 1284,
        "appointments_today": 27,
        "pending": 12,
        "feedback_count": 156,
        "unread": 8,

        "recent_activity": [
            {"title": "New patient registered", "user": "John Smith", "time": "10 minutes ago"},
            {"title": "Appointment scheduled", "user": "Dr. Sarah Johnson", "time": "25 minutes ago"},
            {"title": "Feedback received", "user": "Michael Brown", "time": "1 hour ago"},
        ]
    }

    return render(request, "admin/admin_dashboard.html", context)
  
def add_doctor(request):
    if request.method == "POST":
        # Save later...
        return redirect("manage_doctors")

    return render(request, "admin/doctors/add_doctor.html")


def edit_doctor(request, id):
    doctor = {
        "id": id,
        "name": "Dr. Robert Wilson",
        "specialty": "Neurology",
        "contact": "+1 234-567-8904",
        "email": "robert.w@healthcare.com"
    }

    return render(request, "admin/doctors/edit_doctor.html", {"doctor": doctor})


def view_doctor(request, id):
    doctor = {
        "id": id,
        "name": "Dr. Robert Wilson",
        "specialty": "Neurology",
        "contact": "+1 234-567-8904",
        "email": "robert.w@healthcare.com"
    }

    return render(request, "admin/doctors/view_doctor.html", {"doctor": doctor})
  
def delete_doctor(request, id):
    # TODO: delete from DB in future
    print(f"Doctor with ID {id} deleted")  # debugging output

    return redirect("manage_doctors")
  
def manage_doctors(request):
    doctors = [
        {"id": 1, "name": "Dr. Sarah Johnson", "specialty": "Cardiology", "contact": "+1 234-567-8901", "email": "sarah@clinic.com"},
        {"id": 2, "name": "Dr. Michael Chen", "specialty": "Pediatrics", "contact": "+1 234-567-8902", "email": "michael@clinic.com"},
        {"id": 3, "name": "Dr. Emily Davis", "specialty": "Orthopedics", "contact": "+1 234-567-8903", "email": "emily@clinic.com"},
        {"id": 4, "name": "Dr. Robert Wilson", "specialty": "Neurology", "contact": "+1 234-567-8904", "email": "robert@clinic.com"},
    ]

    return render(request, "admin/manage_doctors.html", {"doctors": doctors})
  
def view_patients(request):
    patients = [
        {"id": "P001", "name": "John Smith", "contact": "+1 234-567-1001", "email": "john.s@email.com", "last_visit": "2024-11-05"},
        {"id": "P002", "name": "Alice Johnson", "contact": "+1 234-567-1002", "email": "alice.j@email.com", "last_visit": "2024-11-08"},
        {"id": "P003", "name": "Robert Brown", "contact": "+1 234-567-1003", "email": "robert.b@email.com", "last_visit": "2024-11-10"},
        {"id": "P004", "name": "Emily Wilson", "contact": "+1 234-567-1004", "email": "emily.w@email.com", "last_visit": "2024-11-11"},
        {"id": "P005", "name": "Michael Davis", "contact": "+1 234-567-1005", "email": "michael.d@email.com", "last_visit": "2024-11-09"},
    ]

    return render(request, "admin/patients/view_patients.html", {"patients": patients})


def patient_details(request, id):
    patient = {
        "id": id,
        "name": "John Smith",
        "contact": "+1 234-567-1001",
        "email": "john.s@email.com",
        "age": 27,
        "gender": "Male",
        "last_visit": "2024-11-05",
        "treatments": [
            {"date": "2024-10-20", "doctor": "Dr. Emily Davis", "notes": "Fracture follow-up"},
            {"date": "2024-11-05", "doctor": "Dr. Sarah Johnson", "notes": "Chest pain consultation"},
        ]
    }

    return render(request, "admin/patients/patient_details.html", {"patient": patient})
  
def view_appointments(request):
    appointments = [
        {"id": "A001", "patient": "John Smith", "doctor": "Dr. Sarah Johnson", 
         "date": "2024-11-12", "time": "09:00 AM", "status": "Scheduled"},

        {"id": "A002", "patient": "Alice Johnson", "doctor": "Dr. Michael Chen", 
         "date": "2024-11-12", "time": "10:30 AM", "status": "Scheduled"},

        {"id": "A003", "patient": "Robert Brown", "doctor": "Dr. Emily Davis",
         "date": "2024-11-11", "time": "02:00 PM", "status": "Completed"},

        {"id": "A004", "patient": "Emily Wilson", "doctor": "Dr. Robert Wilson",
         "date": "2024-11-13", "time": "11:00 AM", "status": "Pending"},

        {"id": "A005", "patient": "Michael Davis", "doctor": "Dr. Sarah Johnson",
         "date": "2024-11-10", "time": "03:30 PM", "status": "Cancelled"},
    ]
    return render(request, "admin/appointments/appointments.html", {"appointments": appointments})
  
def view_feedback(request):
    feedbacks = [
        {
            "id": 1,
            "patient": "John Smith",
            "date": "2024-11-11",
            "rating": 5,
            "message": "Excellent service! Dr. Sarah Johnson was very professional and caring.",
            "is_new": True
        },
        {
            "id": 2,
            "patient": "Alice Johnson",
            "date": "2024-11-10",
            "rating": 5,
            "message": "Great experience with the hospital. Dr. Michael Chen explained everything clearly.",
            "is_new": False
        },
        {
            "id": 3,
            "patient": "Robert Brown",
            "date": "2024-11-09",
            "rating": 4,
            "message": "Good service overall, but had to wait a bit longer than expected for my appointment.",
            "is_new": False
        },
    ]

    return render(request, "admin/feedback/view_feedback.html", {"feedbacks": feedbacks})
  
def register(request):
    return render(request, "doctors/register.html")
