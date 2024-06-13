# Generated by Django 4.2.7 on 2024-05-09 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0010_diary_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="schedules",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]