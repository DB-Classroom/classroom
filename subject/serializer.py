from rest_framework import serializers
from .models import ClassRoom, Student


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"


class StudentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate(self, attrs):
        room = attrs.get("room", None)
        user = attrs.get("student", None)

        if room != None:
            if room.teacher == user:
                raise serializers.ValidationError(
                    {"enroll": "Teacher cannot enroll for students"})
        return super().validate(attrs)
