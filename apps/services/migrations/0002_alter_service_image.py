# Generated by Django 5.0.6 on 2024-06-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="image",
            field=models.ImageField(upload_to="services"),
        ),
    ]