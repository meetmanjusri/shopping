# Generated by Django 3.2.8 on 2021-11-14 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('maplegrocery', '0005_auto_20211027_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='preferred_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='preferred_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Time'),
            preserve_default=False,
        ),
    ]
