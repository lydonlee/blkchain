# Generated by Django 2.1 on 2018-09-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btc', '0010_auto_20180907_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinbar',
            name='m_24hchangepercent',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
