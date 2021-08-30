from rest_framework.decorators import api_view
from rest_framework.response import Response
from .import serializer


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
def createClassroom(request):
    resp = ResponseObject()
    ser = serializer.ClassRoomSerializer(data=request.data)
    if ser.is_valid():
        obj = ser.save()
        resp.success = True
        resp.data = obj.data
        resp.message = "Class room created successfully..."
    else:
        resp.errors = ser.errors
        resp.message = "Class room creatation failed!!!"
    return Response(resp.dict)
