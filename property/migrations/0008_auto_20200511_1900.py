# Generated by Django 2.2.4 on 2020-05-11 16:00
import phonenumbers
from property.models import Flat
from django.db import migrations


def get_pure_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        parse_number = phonenumbers.parse(
            flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(parse_number):
            phone_number = phonenumbers.format_number(
                parse_number,
                phonenumbers.PhoneNumberFormat.E164
            )
            flat.owner_phone_pure = parse_number
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(get_pure_phonenumbers),
    ]