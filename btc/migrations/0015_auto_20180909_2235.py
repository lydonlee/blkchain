# Generated by Django 2.1 on 2018-09-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btc', '0014_auto_20180909_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinbar',
            name='m_website',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
