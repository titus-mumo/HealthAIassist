# Generated by Django 4.1.7 on 2023-07-12 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_usersignsnsymptoms_predicted_disease'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersignsnsymptoms',
            name='date_diagonised',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
