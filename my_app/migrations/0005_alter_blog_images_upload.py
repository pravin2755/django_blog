# Generated by Django 4.0.5 on 2022-07-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alter_blog_images_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='images_upload',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
