from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("classroom/create/", views.createClassroom, name="classroom_created"),
    path("student/create/", views.createStudent, name="student_add"),
]
