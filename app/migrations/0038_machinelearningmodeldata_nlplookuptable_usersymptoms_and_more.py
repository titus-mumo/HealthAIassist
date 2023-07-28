# Generated by Django 4.1.7 on 2023-07-13 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_usersignsnsymptoms_date_diagonised'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineLearningModelData',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('itching', models.BooleanField()),
                ('skin_rash', models.BooleanField()),
                ('nodal_skin_eruptions', models.BooleanField()),
                ('continuous_sneezing', models.BooleanField()),
                ('shivering', models.BooleanField()),
                ('chills', models.BooleanField()),
                ('joint_pain', models.BooleanField()),
                ('acidity', models.BooleanField()),
                ('vomiting', models.BooleanField()),
                ('fatigue', models.BooleanField()),
                ('weight_loss', models.BooleanField()),
                ('restlessness', models.BooleanField()),
                ('cough', models.BooleanField()),
                ('high_fever', models.BooleanField()),
                ('breathlessness', models.BooleanField()),
                ('sweating', models.BooleanField()),
                ('indigestion', models.BooleanField()),
                ('headache', models.BooleanField()),
                ('yellowish_skin', models.BooleanField()),
                ('dark_urine', models.BooleanField()),
                ('nausea', models.BooleanField()),
                ('loss_of_appetite', models.BooleanField(default=False)),
                ('pain_behind_the_eyes', models.BooleanField()),
                ('back_pain', models.BooleanField()),
                ('constipation', models.BooleanField()),
                ('abdominal_pain', models.BooleanField()),
                ('diarrhea', models.BooleanField()),
                ('mild_fever', models.BooleanField()),
                ('yellow_urine', models.BooleanField()),
                ('yellowing_of_eyes', models.BooleanField()),
                ('swelled_lymph_nodes', models.BooleanField()),
                ('malaise', models.BooleanField()),
                ('blurred_vision', models.BooleanField()),
                ('throat_irritation', models.BooleanField()),
                ('redness_of_eyes', models.BooleanField()),
                ('sinus_pressure', models.BooleanField()),
                ('congestion', models.BooleanField()),
                ('runny_nose', models.BooleanField()),
                ('chest_pain', models.BooleanField()),
                ('fast_heart_rate', models.BooleanField()),
                ('cramps', models.BooleanField()),
                ('bruising', models.BooleanField()),
                ('obesity', models.BooleanField()),
                ('swollen_legs', models.BooleanField()),
                ('swollen_blood_vessels', models.BooleanField()),
                ('excessive_hunger', models.BooleanField()),
                ('muscle_weakness', models.BooleanField()),
                ('stiff_neck', models.BooleanField()),
                ('swelling_joints', models.BooleanField()),
                ('movement_stiffness', models.BooleanField()),
                ('loss_of_smell', models.BooleanField()),
                ('loss_of_balance', models.BooleanField()),
                ('passage_of_gases', models.BooleanField()),
                ('internal_itching', models.BooleanField()),
                ('depression', models.BooleanField()),
                ('irritability', models.BooleanField()),
                ('muscle_pain', models.BooleanField()),
                ('red_spots_over_body', models.BooleanField()),
                ('belly_pain', models.BooleanField()),
                ('dischromic_patches', models.BooleanField()),
                ('watering_from_eyes', models.BooleanField()),
                ('increased_appetite', models.BooleanField()),
                ('polyuria', models.BooleanField()),
                ('mucoid_sputum', models.BooleanField()),
                ('rusty_sputum', models.BooleanField()),
                ('visual_disturbances', models.BooleanField()),
                ('blood_transfusion', models.BooleanField()),
                ('unsterile_injections', models.BooleanField()),
                ('blood_in_sputum', models.BooleanField()),
                ('prominent_veins_on_calf', models.BooleanField()),
                ('painful_walking', models.BooleanField()),
                ('irregular_sugar_level', models.BooleanField()),
                ('phlegm', models.BooleanField()),
                ('lethargy', models.BooleanField()),
                ('toxic_look', models.BooleanField()),
                ('disease', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NLPLookUpTable',
            fields=[
                ('sign_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('sign', models.CharField(max_length=255)),
                ('synonym_1', models.CharField(max_length=255)),
                ('synonym_2', models.CharField(max_length=255)),
                ('synonym_3', models.CharField(max_length=255)),
                ('synonym_4', models.CharField(max_length=255)),
                ('synonym_5', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserSymptoms',
            fields=[
                ('patient_sign_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('itching', models.BooleanField()),
                ('skin_rash', models.BooleanField()),
                ('nodal_skin_eruptions', models.BooleanField()),
                ('continuous_sneezing', models.BooleanField()),
                ('shivering', models.BooleanField()),
                ('chills', models.BooleanField()),
                ('joint_pain', models.BooleanField()),
                ('acidity', models.BooleanField()),
                ('vomiting', models.BooleanField()),
                ('fatigue', models.BooleanField()),
                ('weight_loss', models.BooleanField()),
                ('restlessness', models.BooleanField()),
                ('cough', models.BooleanField()),
                ('high_fever', models.BooleanField()),
                ('breathlessness', models.BooleanField()),
                ('sweating', models.BooleanField()),
                ('indigestion', models.BooleanField()),
                ('headache', models.BooleanField()),
                ('yellowish_skin', models.BooleanField()),
                ('dark_urine', models.BooleanField()),
                ('nausea', models.BooleanField()),
                ('loss_of_appetite', models.BooleanField(default=False)),
                ('pain_behind_the_eyes', models.BooleanField()),
                ('back_pain', models.BooleanField()),
                ('constipation', models.BooleanField()),
                ('abdominal_pain', models.BooleanField()),
                ('diarrhea', models.BooleanField()),
                ('mild_fever', models.BooleanField()),
                ('yellow_urine', models.BooleanField()),
                ('yellowing_of_eyes', models.BooleanField()),
                ('swelled_lymph_nodes', models.BooleanField()),
                ('malaise', models.BooleanField()),
                ('blurred_vision', models.BooleanField()),
                ('throat_irritation', models.BooleanField()),
                ('redness_of_eyes', models.BooleanField()),
                ('sinus_pressure', models.BooleanField()),
                ('congestion', models.BooleanField()),
                ('runny_nose', models.BooleanField()),
                ('chest_pain', models.BooleanField()),
                ('fast_heart_rate', models.BooleanField()),
                ('cramps', models.BooleanField()),
                ('bruising', models.BooleanField()),
                ('obesity', models.BooleanField()),
                ('swollen_legs', models.BooleanField()),
                ('swollen_blood_vessels', models.BooleanField()),
                ('excessive_hunger', models.BooleanField()),
                ('muscle_weakness', models.BooleanField()),
                ('stiff_neck', models.BooleanField()),
                ('swelling_joints', models.BooleanField()),
                ('movement_stiffness', models.BooleanField()),
                ('loss_of_smell', models.BooleanField()),
                ('loss_of_balance', models.BooleanField()),
                ('passage_of_gases', models.BooleanField()),
                ('internal_itching', models.BooleanField()),
                ('depression', models.BooleanField()),
                ('irritability', models.BooleanField()),
                ('muscle_pain', models.BooleanField()),
                ('red_spots_over_body', models.BooleanField()),
                ('belly_pain', models.BooleanField()),
                ('dischromic_patches', models.BooleanField()),
                ('watering_from_eyes', models.BooleanField()),
                ('increased_appetite', models.BooleanField()),
                ('polyuria', models.BooleanField()),
                ('mucoid_sputum', models.BooleanField()),
                ('rusty_sputum', models.BooleanField()),
                ('visual_disturbances', models.BooleanField()),
                ('blood_transfusion', models.BooleanField()),
                ('unsterile_injections', models.BooleanField()),
                ('blood_in_sputum', models.BooleanField()),
                ('prominent_veins_on_calf', models.BooleanField()),
                ('painful_walking', models.BooleanField()),
                ('irregular_sugar_level', models.BooleanField()),
                ('phlegm', models.BooleanField()),
                ('lethargy', models.BooleanField()),
                ('toxic_look', models.BooleanField()),
                ('predicted_disease', models.CharField(default='', max_length=255)),
                ('date_diagonised', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='MLModelData',
        ),
        migrations.DeleteModel(
            name='NLPTable',
        ),
        migrations.DeleteModel(
            name='UserSignsnSymptoms',
        ),
    ]
