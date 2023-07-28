# Generated by Django 4.1.7 on 2023-06-29 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_machinelearningdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('disease', models.CharField(max_length=100)),
                ('medicine', models.CharField(max_length=100)),
                ('supportive_care', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]