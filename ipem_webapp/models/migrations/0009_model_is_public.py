# Generated by Django 4.1.7 on 2023-05-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("models", "0008_developmentactivity_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="model",
            name="is_public",
            field=models.BooleanField(default=False),
        ),
    ]
