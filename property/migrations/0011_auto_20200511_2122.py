# Generated by Django 2.2.4 on 2020-05-11 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20200511_2109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'verbose_name': 'Жалобы'},
        ),
        migrations.AlterModelOptions(
            name='flat',
            options={'verbose_name': 'Квартиры'},
        ),
    ]
