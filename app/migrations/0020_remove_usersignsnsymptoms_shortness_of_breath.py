# Generated by Django 4.1.7 on 2023-07-06 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_remove_mlmodeldata_shortness_of_breath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersignsnsymptoms',
            name='shortness_of_breath',
        ),
    ]