# Generated by Django 2.0.6 on 2018-10-22 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='deposit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='withdrawl',
            field=models.IntegerField(default=0),
        ),
    ]
