# Generated by Django 4.2.7 on 2024-03-03 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_remove_diary_created_at_remove_diary_updated_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="diary",
            name="cat",
        ),
        migrations.AlterField(
            model_name="diary",
            name="date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="日付"
            ),
        ),
        migrations.AlterField(
            model_name="diary",
            name="text",
            field=models.TextField(verbose_name="本文"),
        ),
        migrations.AlterField(
            model_name="diary",
            name="title",
            field=models.CharField(max_length=200, verbose_name="タイトル"),
        ),
    ]
