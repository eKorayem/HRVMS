# Generated by Django 5.0.3 on 2024-04-18 11:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_vacation_substitute_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='substitute_employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='substitute_vacations', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
