# Generated by Django 3.2.8 on 2022-01-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_auto_20220111_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_postcode',
            field=models.CharField(default='XXX 4Y', max_length=20),
            preserve_default=False,
        ),
    ]
