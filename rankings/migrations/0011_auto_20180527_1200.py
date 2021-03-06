# Generated by Django 2.0.5 on 2018-05-27 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0010_auto_20180517_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
