# Generated by Django 4.0.10 on 2023-04-25 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_remove_layer_generation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layer',
            name='generation_type',
        ),
        migrations.AddField(
            model_name='layer',
            name='generation',
            field=models.CharField(choices=[('CURRENT', 'Current'), ('PREVIOUS_1', 'n-1'), ('PREVIOUS_2', 'n-2'), ('PREVIOUS_3', 'n-3'), ('FOLLOWING_1', 'n+1'), ('FOLLOWING_2', 'n+2'), ('FOLLOWING_3', 'n+3')], default='CURRENT', max_length=11),
        ),
    ]
