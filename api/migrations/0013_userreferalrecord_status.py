# Generated by Django 3.2.6 on 2021-09-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_discountprice_discountlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreferalrecord',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('done', 'done')], default='pending', max_length=10),
        ),
    ]