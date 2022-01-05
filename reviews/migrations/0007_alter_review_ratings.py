# Generated by Django 3.2.8 on 2022-01-04 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20220102_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ratings',
            field=models.DecimalField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], decimal_places=2, default=5.0, max_digits=5),
        ),
    ]