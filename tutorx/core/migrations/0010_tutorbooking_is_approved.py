# Generated by Django 5.0.1 on 2024-04-13 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_tutorrating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorbooking',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]