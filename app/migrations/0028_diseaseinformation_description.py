# Generated by Django 4.1.7 on 2023-07-10 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_diseaseinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseaseinformation',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
