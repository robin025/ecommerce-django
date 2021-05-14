# Generated by Django 3.0.8 on 2020-07-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20200719_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_tile', models.CharField(max_length=50)),
                ('head1', models.CharField(default='', max_length=100)),
                ('head2', models.CharField(default='', max_length=100)),
                ('head3', models.CharField(default='', max_length=100)),
                ('publish_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]
