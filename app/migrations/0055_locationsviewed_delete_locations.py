# Generated by Django 4.1.7 on 2023-07-18 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0054_locations'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationsViewed',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date_viewed', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Locations',
        ),
    ]
