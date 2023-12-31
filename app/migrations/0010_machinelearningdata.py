# Generated by Django 4.1.7 on 2023-06-21 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_patientsigns_conjunctivities'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineLearningData',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('fever', models.BooleanField()),
                ('cough', models.BooleanField()),
                ('sore_throat', models.BooleanField()),
                ('body_aches', models.BooleanField()),
                ('chills', models.BooleanField()),
                ('sweating', models.BooleanField()),
                ('headache', models.BooleanField()),
                ('nausea', models.BooleanField()),
                ('vomiting', models.BooleanField()),
                ('weight_loss', models.BooleanField()),
                ('night_sweats', models.BooleanField()),
                ('weakness', models.BooleanField()),
                ('fatigue', models.BooleanField()),
                ('abdominal_pain', models.BooleanField()),
                ('diarrhea', models.BooleanField()),
                ('dehydration', models.BooleanField(default=False)),
                ('rash', models.BooleanField()),
                ('muscle_pain', models.BooleanField()),
                ('back_pain', models.BooleanField()),
                ('stiff_neck', models.BooleanField()),
                ('confusion', models.BooleanField()),
                ('runny_nose', models.BooleanField()),
                ('tiredness', models.BooleanField()),
                ('shortness_of_breath', models.BooleanField()),
                ('loss_of_appetite', models.BooleanField()),
                ('chest_pain', models.BooleanField()),
                ('wheezing', models.BooleanField()),
                ('disease', models.CharField(max_length=255)),
            ],
        ),
    ]
