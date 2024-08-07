# Generated by Django 4.2.7 on 2024-02-22 04:20

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Diary",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="日付"
                    ),
                ),
                ("title", models.CharField(max_length=40, verbose_name="タイトル")),
                ("text", models.CharField(max_length=200, verbose_name="本文")),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="作成日時"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, null=True, verbose_name="編集日時"),
                ),
            ],
        ),
    ]
