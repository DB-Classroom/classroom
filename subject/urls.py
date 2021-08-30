from django.urls import path
from . import views

urlpatterns = [
    path("classroom/create/", views.createClassroom, name="classroom_created")
]
