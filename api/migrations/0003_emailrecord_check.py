# Generated by Django 3.2.6 on 2021-09-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_emailrecord_sendstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailrecord',
            name='check',
            field=models.CharField(choices=[('pending', 'pending'), ('click', 'click')], default='pending', max_length=120),
        ),
    ]
