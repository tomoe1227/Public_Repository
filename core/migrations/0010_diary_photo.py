# Generated by Django 4.2.7 on 2024-04-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_remove_schedule_reminder_sent_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="diary",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="diary_photos/"),
        ),
    ]