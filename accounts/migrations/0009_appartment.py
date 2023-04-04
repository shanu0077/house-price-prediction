# Generated by Django 4.1.7 on 2023-03-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_hotelowner_delete_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appartment',
            fields=[
                ('ap_id', models.AutoField(primary_key=True, serialize=False)),
                ('appartmentname', models.CharField(max_length=50, unique=True, verbose_name='firstname')),
                ('propertytype', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField(max_length=50)),
                ('year', models.IntegerField(max_length=50)),
                ('propertysize', models.IntegerField(max_length=50)),
                ('bedrooms', models.IntegerField(max_length=50)),
                ('bathrooms', models.IntegerField(max_length=50)),
                ('furnishing', models.CharField(max_length=100)),
                ('availability', models.CharField(max_length=100)),
                ('rent', models.CharField(max_length=100)),
                ('price', models.IntegerField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('propdesc', models.CharField(max_length=100)),
            ],
        ),
    ]