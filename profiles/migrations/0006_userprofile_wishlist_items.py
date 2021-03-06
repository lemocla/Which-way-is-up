# Generated by Django 3.2.8 on 2021-12-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0013_alter_artwork_related_items'),
        ('profiles', '0005_alter_userprofile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wishlist_items',
            field=models.ManyToManyField(to='artworks.Artwork'),
        ),
    ]
