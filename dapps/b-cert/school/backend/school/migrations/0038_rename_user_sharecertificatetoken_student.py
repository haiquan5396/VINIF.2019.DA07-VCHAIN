# Generated by Django 4.0.3 on 2022-03-18 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0037_sharecertificatetoken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharecertificatetoken',
            old_name='user',
            new_name='student',
        ),
    ]
