# Generated by Django 5.0.1 on 2024-04-11 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_completedjob_ongoingjob'),
        ('user', '0037_tutor_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorrequest',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='tutorrequest',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='tutorrequest',
            name='status',
        ),
        migrations.AddField(
            model_name='tutorrequest',
            name='client',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutorrequest',
            name='tutor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.tutor'),
            preserve_default=False,
        ),
    ]
