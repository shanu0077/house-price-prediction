# Generated by Django 4.1.4 on 2023-03-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_hotelowner_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='phone_num',
            field=models.IntegerField(default=0),
        ),
    ]
