# Generated by Django 4.1.7 on 2023-05-12 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("models", "0010_developmentactivity_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="model",
            name="owner",
            field=models.ForeignKey(
                default=3,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="model",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
