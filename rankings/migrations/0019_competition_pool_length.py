# Generated by Django 2.1.5 on 2019-03-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0018_auto_20180819_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='pool_length',
            field=models.IntegerField(choices=[(50, 'Long course'), (25, 'Short Course')], default=50),
        ),
    ]