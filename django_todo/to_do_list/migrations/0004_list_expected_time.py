# Generated by Django 3.1.6 on 2021-02-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0003_remove_list_time_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='expected_time',
            field=models.IntegerField(blank=True, default=15),
        ),
    ]
