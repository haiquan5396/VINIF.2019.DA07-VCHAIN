# Generated by Django 2.2.24 on 2021-06-29 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20210627_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='avatar',
            field=models.ImageField(default='', upload_to='profile_pics/uni_pics'),
        ),
    ]