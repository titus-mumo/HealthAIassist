# Generated by Django 4.1.7 on 2023-07-12 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_inputfield_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='contact',
            field=models.CharField(max_length=15),
        ),
    ]