# Generated by Django 3.2.8 on 2021-10-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maplegrocery', '0004_auto_20211026_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_card',
        ),
        migrations.AddField(
            model_name='order',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
