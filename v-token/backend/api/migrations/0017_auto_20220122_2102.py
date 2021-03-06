# Generated by Django 3.2.8 on 2022-01-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_fabricftcontract_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FabricFTContract',
        ),
        migrations.RemoveField(
            model_name='nftcontract',
            name='abi',
        ),
        migrations.RemoveField(
            model_name='nftcontract',
            name='address',
        ),
        migrations.RemoveField(
            model_name='nftcontract',
            name='compiled_code',
        ),
        migrations.RemoveField(
            model_name='nftcontract',
            name='max_supply',
        ),
        migrations.AddField(
            model_name='ftcontract',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Fail', 'Fail'), ('Success', 'Success')], default='Pending', max_length=16),
        ),
        migrations.AddField(
            model_name='ftcontract',
            name='user_defined_network',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='nftcontract',
            name='user_defined_network',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
