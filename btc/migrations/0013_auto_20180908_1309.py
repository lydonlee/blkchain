# Generated by Django 2.1 on 2018-09-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btc', '0012_auto_20180907_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinbar',
            name='m_24hchange',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
