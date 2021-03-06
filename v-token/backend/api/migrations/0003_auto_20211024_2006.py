# Generated by Django 3.2.8 on 2021-10-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211024_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='ftcontract',
            name='burnable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ftcontract',
            name='pausable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ftcontract',
            name='token_cap',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nftcontract',
            name='token_cap',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
