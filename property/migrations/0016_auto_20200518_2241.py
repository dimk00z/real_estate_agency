# Generated by Django 2.2.4 on 2020-05-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20200513_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='owners', to='property.Flat', verbose_name='квартиры в собственности'),
        ),
    ]
