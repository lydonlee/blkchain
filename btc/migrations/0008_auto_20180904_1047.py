# Generated by Django 2.1 on 2018-09-04 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btc', '0007_auto_20180904_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinexchanges',
            name='m_exchange',
            field=models.CharField(max_length=20),
        ),
    ]
