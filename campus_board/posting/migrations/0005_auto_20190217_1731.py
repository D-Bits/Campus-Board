# Generated by Django 2.1.5 on 2019-02-18 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0004_post_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='sale_id',
        ),
    ]