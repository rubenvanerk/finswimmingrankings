# Generated by Django 2.0.5 on 2018-06-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0013_individualresult_extra_analysis_time_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='name',
            field=models.CharField(max_length=60, null=True, unique=True),
        ),
    ]
