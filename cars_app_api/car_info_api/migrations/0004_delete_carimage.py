# Generated by Django 4.1.1 on 2022-09-29 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_info_api', '0003_image_modelimage_versionimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarImage',
        ),
    ]
