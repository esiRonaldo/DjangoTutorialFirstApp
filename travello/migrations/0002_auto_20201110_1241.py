# Generated by Django 2.2.12 on 2020-11-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='price',
            field=models.IntegerField(),
        ),
    ]
