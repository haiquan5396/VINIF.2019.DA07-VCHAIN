# Generated by Django 3.2.8 on 2021-10-24 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_ftcontract_initial_supply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ftcontract',
            old_name='token_cap',
            new_name='max_supply',
        ),
        migrations.RenameField(
            model_name='nftcontract',
            old_name='token_cap',
            new_name='max_supply',
        ),
    ]
