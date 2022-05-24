# Generated by Django 4.0.4 on 2022-05-24 02:34

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proevent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('image', models.ImageField(blank=True, upload_to='events/images')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('year', 'month'),
            },
        ),
        migrations.RemoveField(
            model_name='event',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]