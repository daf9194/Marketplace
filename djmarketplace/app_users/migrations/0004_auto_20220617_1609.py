# Generated by Django 3.2.1 on 2022-06-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0003_auto_20220617_1609'),
        ('app_users', '0003_auto_20220605_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='basket',
            field=models.ManyToManyField(blank=True, to='app_goods.GoodBasket'),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_buy',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
