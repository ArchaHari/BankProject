# Generated by Django 4.2.2 on 2023-07-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_addamountmodel_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawmodel',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
