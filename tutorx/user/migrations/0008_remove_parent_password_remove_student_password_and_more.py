# Generated by Django 5.0.1 on 2024-03-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_customuser_level_customuser_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
