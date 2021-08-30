# Generated by Django 3.1.2 on 2021-08-30 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('code', models.CharField(default='gyl06X', max_length=6)),
                ('subject_name', models.CharField(max_length=255)),
                ('image', models.TextField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('join_at', models.TimeField(auto_created=True, auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('join_by', models.CharField(choices=[('link', 'link'), ('invite', 'invite')], default='link', max_length=10)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.classroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
