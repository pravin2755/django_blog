# Generated by Django 4.0.5 on 2022-07-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='images_upload',
            field=models.ImageField(null=True, upload_to='upload_images'),
        ),
    ]
