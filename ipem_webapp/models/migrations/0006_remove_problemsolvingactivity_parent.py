# Generated by Django 4.1.7 on 2023-04-30 17:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("models", "0005_model_stream"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="problemsolvingactivity",
            name="parent",
        ),
    ]