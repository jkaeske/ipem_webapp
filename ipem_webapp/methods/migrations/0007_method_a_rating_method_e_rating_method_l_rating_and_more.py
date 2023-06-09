# Generated by Django 4.1.7 on 2023-04-30 17:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("models", "0005_model_stream"),
        ("methods", "0006_method_s_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="method",
            name="a_rating",
            field=models.PositiveSmallIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(5)]
            ),
        ),
        migrations.AddField(
            model_name="method",
            name="e_rating",
            field=models.PositiveSmallIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(5)]
            ),
        ),
        migrations.AddField(
            model_name="method",
            name="l_rating",
            field=models.PositiveSmallIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(5)]
            ),
        ),
        migrations.AddField(
            model_name="method",
            name="n_rating",
            field=models.PositiveSmallIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(5)]
            ),
        ),
        migrations.AddField(
            model_name="method",
            name="p_rating",
            field=models.PositiveSmallIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(5)]
            ),
        ),
        migrations.AddField(
            model_name="method",
            name="t_rating",
            field=models.PositiveSmallIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(5)]
            ),
        ),
        migrations.CreateModel(
            name="MethodRegistry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rating",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(5)],
                    ),
                ),
                (
                    "development_activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="models.developmentactivity",
                    ),
                ),
                (
                    "method",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="methods.method"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="method",
            name="activity",
            field=models.ManyToManyField(
                through="methods.MethodRegistry", to="models.developmentactivity"
            ),
        ),
    ]
