# Generated by Django 3.1.6 on 2021-02-12 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0005_list_frequency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(help_text='Day of the event', verbose_name='Day of the event')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='Starting time')),
                ('end_time', models.TimeField(help_text='Final time', verbose_name='Final time')),
                ('notes', models.TextField(blank=True, help_text='Textual Notes', null=True, verbose_name='Textual Notes')),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
    ]
