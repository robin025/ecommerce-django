# Generated by Django 3.0.8 on 2020-07-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id_blog', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name_blog', models.CharField(max_length=50)),
                ('contact_email_blog', models.CharField(max_length=100)),
                ('contact_phone_blog', models.CharField(max_length=15)),
                ('contact_desc_blog', models.CharField(max_length=1000)),
            ],
        ),
    ]
