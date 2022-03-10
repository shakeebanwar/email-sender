# Generated by Django 3.2.6 on 2021-09-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_rating_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.FloatField(default=0),
        ),
    ]
