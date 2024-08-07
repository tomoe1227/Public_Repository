# Generated by Django 4.2.7 on 2024-03-27 07:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_securityquestion"),
    ]

    operations = [
        migrations.AddField(
            model_name="cat",
            name="birthday",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cat",
            name="food_amount",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cat",
            name="gender",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="cat",
            name="health_status",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cat",
            name="personality",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cat",
            name="weight",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
    ]
