# Generated by Django 2.0.1 on 2018-03-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0005_auto_20180301_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='type_of_timekeeping',
            field=models.IntegerField(choices=[(0, 'Unknown'), (1, 'Electronic'), (2, 'By hand')], default=1),
        ),
    ]
