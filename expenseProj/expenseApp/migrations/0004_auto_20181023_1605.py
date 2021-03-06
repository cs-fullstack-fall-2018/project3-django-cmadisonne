# Generated by Django 2.0.6 on 2018-10-23 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApp', '0003_auto_20181022_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expensemodel',
            old_name='username',
            new_name='username_fk',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='username',
            new_name='account_fk',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='date',
            new_name='timeOfTransaction',
        ),
        migrations.RemoveField(
            model_name='expensemodel',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='expensemodel',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='expensemodel',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='expensemodel',
            name='password',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='deposit',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='withdrawl',
        ),
        migrations.AddField(
            model_name='expensemodel',
            name='checking',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expensemodel',
            name='timeCreated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='transaction',
            name='depositOrWithdrawl',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expensemodel',
            name='emergency',
            field=models.IntegerField(default=0),
        ),
    ]
