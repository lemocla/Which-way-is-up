# Generated by Django 3.2.8 on 2021-12-23 11:46

from django.db import migrations, models
import portfolio.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', portfolio.fields.CaseInsensitiveCharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Shop categories',
                'ordering': ['name'],
            },
        ),
    ]
