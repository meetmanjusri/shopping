# Generated by Django 2.2.4 on 2021-09-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maplegrocery', '0002_remove_order_payment_cvv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]