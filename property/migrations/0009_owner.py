# Generated by Django 2.2.4 on 2020-05-11 17:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20200511_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phone_number', models.CharField(max_length=20, verbose_name='номер телефона владельца')),
                ('normalized_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='нормализованный номер телефона владельца')),
                ('flats', models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='квартиры в собственности')),
            ],
            options={
                'verbose_name': 'владелец',
                'verbose_name_plural': 'владельцы',
            },
        ),
    ]