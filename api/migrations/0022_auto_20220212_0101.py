# Generated by Django 3.2.6 on 2022-02-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_emailreferalrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailreferalrecord',
            name='status',
        ),
        migrations.AddField(
            model_name='emailreferalrecord',
            name='creation',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
