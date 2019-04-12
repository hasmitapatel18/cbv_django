# Generated by Django 2.1.7 on 2019-04-11 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('g2', '0003_auto_20190407_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image_u',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.CharField(default='comedy', max_length=100),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='g2.Film'),
        ),
    ]
