# Generated by Django 2.2.24 on 2021-07-08 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0024_student_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='register_id',
            field=models.CharField(default='', max_length=128, null=True),
        ),
    ]
