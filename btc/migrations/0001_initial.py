# Generated by Django 2.1 on 2018-08-26 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coinbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_symbol', models.CharField(max_length=10)),
                ('m_date', models.DateTimeField()),
                ('m_open', models.FloatField(default=0)),
                ('m_high', models.FloatField(default=0)),
                ('m_low', models.FloatField(default=0)),
                ('m_close', models.FloatField(default=0)),
                ('m_vol', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Coinexchanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_exchange', models.CharField(max_length=10)),
                ('m_name', models.CharField(max_length=20)),
                ('m_area', models.CharField(max_length=5)),
                ('m_website', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='coinbar',
            name='m_coinexchanges',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btc.Coinexchanges'),
        ),
    ]
