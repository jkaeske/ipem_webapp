# Generated by Django 4.0.10 on 2023-03-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('methods', '0002_method_alternative_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='method',
            name='abstract',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='method',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]