# Generated by Django 4.1.7 on 2023-07-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_feedback_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
