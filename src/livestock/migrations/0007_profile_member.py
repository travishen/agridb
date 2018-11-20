# Generated by Django 2.0.9 on 2018-11-20 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0008_auto_20181115_1141'),
        ('livestock', '0006_auto_20181120_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='household.Member', verbose_name='Member'),
            preserve_default=False,
        ),
    ]
