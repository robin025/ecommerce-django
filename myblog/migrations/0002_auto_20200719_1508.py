# Generated by Django 3.0.8 on 2020-07-19 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='BlogContact',
        ),
    ]
