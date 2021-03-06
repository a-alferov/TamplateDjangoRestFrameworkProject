# Generated by Django 3.2.8 on 2021-11-01 09:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('created_date',
                 models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('uri', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('created_date',
                 models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date',
                 models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('created_date',
                 models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('tag', models.SlugField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                   to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date',
                 models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('toppings',
                 models.ManyToManyField(blank=True, related_name='pizza', to='api.Topping')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('reporter',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reporter')),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
    ]
