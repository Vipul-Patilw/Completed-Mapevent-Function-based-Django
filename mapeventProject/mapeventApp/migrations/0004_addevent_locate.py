# Generated by Django 4.0.3 on 2022-08-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapeventApp', '0003_locateevent_addevent_city_addevent_eventermail'),
    ]

    operations = [
        migrations.AddField(
            model_name='addevent',
            name='locate',
            field=models.CharField(default='dadar', max_length=122),
        ),
    ]
