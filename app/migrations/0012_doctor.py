# Generated by Django 4.1.7 on 2023-07-01 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_records'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('doctor_name', models.CharField(max_length=255)),
                ('health_institution', models.CharField(max_length=255)),
                ('disease_of_specialization', models.CharField(max_length=255)),
                ('doctor_email', models.EmailField(max_length=255, unique=True)),
                ('contact', models.BigIntegerField()),
                ('latiitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]