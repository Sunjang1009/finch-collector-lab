# Generated by Django 4.2.2 on 2023-06-27 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='gender',
            field=models.CharField(choices=[('Female', 'female'), ('Male', 'male')], default='female', max_length=10),
        ),
    ]
