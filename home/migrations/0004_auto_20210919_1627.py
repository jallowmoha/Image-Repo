# Generated by Django 3.2.3 on 2021-09-19 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_img_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
