# Generated by Django 3.2.8 on 2021-12-22 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_remove_portfolio_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.portfoliocategory'),
        ),
    ]