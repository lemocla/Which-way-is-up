# Generated by Django 3.2.8 on 2022-01-11 18:21

import checkout.models
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20220109_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_country',
            field=django_countries.fields.CountryField(countries=checkout.models.Order.G8Countries, max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
