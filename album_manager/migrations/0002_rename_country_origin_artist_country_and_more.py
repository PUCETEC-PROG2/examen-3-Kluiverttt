# Generated by Django 4.2 on 2024-08-05 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='country_origin',
            new_name='country',
        ),
        migrations.AlterField(
            model_name='album',
            name='portada',
            field=models.ImageField(upload_to='portada/'),
        ),
    ]
