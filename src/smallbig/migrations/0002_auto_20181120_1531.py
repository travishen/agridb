# Generated by Django 2.1.2 on 2018-11-20 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0008_auto_20181115_1141'),
        ('smallbig', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlordrent',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='household.Year', verbose_name='Year'),
        ),
        migrations.AddField(
            model_name='landlordretire',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='household.Year', verbose_name='Year'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='household.Year', verbose_name='Year'),
        ),
        migrations.AddField(
            model_name='tenanttransfer',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='household.Year', verbose_name='Year'),
        ),
    ]
