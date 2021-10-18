# Generated by Django 3.2.8 on 2021-10-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0006_alter_coin_id'),
        ('watchlist', '0004_alter_watchlist_coins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='coins',
            field=models.ManyToManyField(blank=True, related_name='coins', to='coins.Coin'),
        ),
    ]
