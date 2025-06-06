# Generated by Django 2.2.24 on 2025-06-01 13:01

from django.db import migrations


def owners_and_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.iterator(chunk_size=200):
        owners = Owner.objects.filter(owner_pure_phone=flat.owner_pure_phone)
        if owners:
            for owner in owners:
                owner.owner_flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20250601_1521'),
    ]

    operations = [
        migrations.RunPython(owners_and_flats)
    ]
