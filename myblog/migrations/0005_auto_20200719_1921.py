# Generated by Django 3.0.8 on 2020-07-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20200719_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='text_head1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='text_head2',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='text_head3',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head3',
            field=models.CharField(default='', max_length=100),
        ),
    ]
