# Generated by Django 3.0.8 on 2020-07-14 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order_order_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_no',
        ),
    ]
