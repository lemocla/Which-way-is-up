# Generated by Django 3.2.8 on 2021-12-21 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_portofoliocategory_portfoliocategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfoliocategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'Portfolio categories'},
        ),
    ]