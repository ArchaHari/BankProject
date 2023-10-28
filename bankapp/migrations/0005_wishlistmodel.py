# Generated by Django 4.2.2 on 2023-07-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0004_newsfeedmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlistmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('date', models.DateField()),
            ],
        ),
    ]