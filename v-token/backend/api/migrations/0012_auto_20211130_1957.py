# Generated by Django 3.2.8 on 2021-11-30 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_linkedftcontracts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('network_id', models.PositiveIntegerField(null=True)),
                ('chain_id', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ftcontract',
            name='chain_id',
        ),
        migrations.RemoveField(
            model_name='nftcontract',
            name='chain_id',
        ),
        migrations.AddField(
            model_name='ftcontract',
            name='network',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.network'),
        ),
        migrations.AddField(
            model_name='nftcontract',
            name='network',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.network'),
        ),
    ]