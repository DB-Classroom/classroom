from djongo import models
from django.utils.crypto import get_random_string
from authentication.models import User
from uuid import uuid4


class ClassRoom(models.Model):
    code = models.CharField(primary_key=True, max_length=6,
                            default=get_random_string(6))
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=255)
    image = models.TextField()

    def __str__(self) -> str:
        return self.subject_name


class Student(models.Model):
    JOIN_BY = (("link", "link"), ("invite", "invite"))

    id = models.UUIDField(primary_key=True, default=uuid4)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    join_by = models.CharField(
        max_length=10, choices=JOIN_BY, default=JOIN_BY[0][0])
    join_at = models.TimeField(auto_created=True, auto_now=True)

    def __str__(self) -> str:
        return self.student.email + "-" + self.room.subject_name

    class Meta:
        unique_together = ("student", "room")
