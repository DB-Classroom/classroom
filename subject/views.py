from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .import serializer
from django.http import HttpRequest


class ResponseObject:
    def __init__(self) -> None:
        self.success = False
        self.data = {}
        self.errors = {}
        self.message = ""

    @property
    def dict(self):
        return vars(self)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createClassroom(request: HttpRequest):
    resp = ResponseObject()
    req = request.data
    req["teacher"] = request.user.id
    ser = serializer.ClassRoomSerializer(data=req)
    if ser.is_valid():
        _ = ser.save()
        resp.success = True
        resp.data = ser.data
        resp.message = "Class room created successfully..."
    else:
        resp.errors = ser.errors
        resp.message = "Class room creatation failed!!!"
    return Response(resp.dict)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createStudent(request: HttpRequest):
    resp = ResponseObject()
    req = request.data
    req["student"] = request.user.id
    ser = serializer.StudentAddSerializer(data=req)
    if ser.is_valid():
        ser.save()
        resp.success = True
        resp.data = ser.data
        resp.message = "Student added successfully..."
    else:
        resp.errors = ser.errors
        resp.message = "Unable to add student!!!"
    return Response(resp.dict)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard(request: HttpRequest):
    user = request.user
    resp = ResponseObject()
    resp.data["class_rooms"] = serializer.ClassRoomSerializer(
        user.classroom_set.all(), many=True).data
    resp.data["subjects"] = []
    resp.success = True
    for x in user.student_set.all():
        resp.data["subjects"].append(
            serializer.ClassRoomSerializer(x.room).data)

    return Response(resp.dict)
