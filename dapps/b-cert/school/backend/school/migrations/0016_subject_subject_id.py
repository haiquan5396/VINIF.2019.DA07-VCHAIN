# Generated by Django 2.2.24 on 2021-07-01 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_class_class_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_id',
            field=models.CharField(default='', max_length=10, null=True),
        ),
    ]
