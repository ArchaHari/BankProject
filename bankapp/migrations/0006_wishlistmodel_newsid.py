# Generated by Django 4.2.2 on 2023-07-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_wishlistmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistmodel',
            name='newsid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
