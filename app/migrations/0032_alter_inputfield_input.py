# Generated by Django 4.1.7 on 2023-07-12 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_alter_inputfield_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputfield',
            name='input',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
