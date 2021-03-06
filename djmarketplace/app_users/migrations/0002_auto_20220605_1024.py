# Generated by Django 3.2.1 on 2022-06-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('JUN', 'jun'), ('MDL', 'mdl'), ('SEN', 'sen')], default='JUN', max_length=3),
        ),
    ]
