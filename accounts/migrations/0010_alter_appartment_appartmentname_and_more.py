# Generated by Django 4.1.7 on 2023-03-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_appartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appartment',
            name='appartmentname',
            field=models.CharField(max_length=50, verbose_name='firstname'),
        ),
        migrations.AlterField(
            model_name='appartment',
            name='propertytype',
            field=models.CharField(max_length=50),
        ),
    ]