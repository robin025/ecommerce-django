# Generated by Django 3.0.8 on 2020-07-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_no',
            field=models.IntegerField(default=1),
        ),
    ]
