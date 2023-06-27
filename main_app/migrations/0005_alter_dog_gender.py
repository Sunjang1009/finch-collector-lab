# Generated by Django 4.2.2 on 2023-06-27 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_dog_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='female', max_length=10),
        ),
    ]