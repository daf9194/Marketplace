# Generated by Django 3.2.1 on 2022-06-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_auto_20220605_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('JUN', 'jun'), ('MDL', 'mdl'), ('SEN', 'sen')], default='JUN', max_length=3),
        ),
    ]