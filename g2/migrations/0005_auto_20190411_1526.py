# Generated by Django 2.1.7 on 2019-04-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g2', '0004_auto_20190411_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]