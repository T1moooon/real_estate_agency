# Generated by Django 2.2.24 on 2025-06-03 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20250604_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(blank=True, db_index=True, null=True, verbose_name='Новостройка'),
        ),
    ]
