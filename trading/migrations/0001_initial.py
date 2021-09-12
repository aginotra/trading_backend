# Generated by Django 3.0.5 on 2021-06-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('crypto_currency', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('amount', models.FloatField(default='0.00')),
                ('profit_loss_amt', models.FloatField(default='0.00')),
                ('description', models.TextField(default=None)),
                ('share_date', models.DateTimeField(default=None)),
            ],
        ),
    ]
