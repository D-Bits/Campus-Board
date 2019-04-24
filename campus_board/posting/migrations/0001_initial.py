# Generated by Django 2.1.5 on 2019-02-14 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField(help_text='Enter 9-digit student id', max_length=9)),
                ('created', models.DateTimeField(auto_now=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post_type', models.CharField(choices=[('Sale', 'Sale'), ('Housing', 'Housing'), ('Ridesharing', 'Ridesharing')], default='Housing', max_length=11)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(help_text='Describe your post, and leave contact info.')),
                ('sale_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posting.Author')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
