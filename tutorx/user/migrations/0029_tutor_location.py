# Generated by Django 5.0.1 on 2024-04-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_client_email_client_full_name_client_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='location',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
