# Generated by Django 4.1.1 on 2022-09-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_info_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('brand_id', models.AutoField(db_column='brand_id', primary_key=True, serialize=False, unique=True)),
                ('brand_name', models.CharField(blank=True, max_length=70, null=True)),
            ],
            options={
                'db_table': 'brands',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
