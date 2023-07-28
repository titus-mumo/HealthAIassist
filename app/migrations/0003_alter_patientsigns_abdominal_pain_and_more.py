# Generated by Django 4.1.7 on 2023-06-07 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_patientsigns_dehydration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientsigns',
            name='abdominal_pain',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='back_pain',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='body_aches',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='chest_pain',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='chills',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='confusion',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='conjunctivities',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='cough',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='diarrhea',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='fatigue',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='fever',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='headache',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='laundice',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='loss_of_appetite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='muscle_pain',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='nausea',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='night_sweats',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='rash',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='runny_nose',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='seizures',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='shortness_of_breath',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='sore_throat',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='stiff_neck',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='sweating',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='swollen_lymph_nodes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='swollen_salivary_glands',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='tiredness',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='vomiting',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='weakness',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='weight_loss',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientsigns',
            name='wheezing',
            field=models.BooleanField(default=False),
        ),
    ]
