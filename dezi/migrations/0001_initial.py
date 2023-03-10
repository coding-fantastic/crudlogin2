# Generated by Django 4.1.7 on 2023-03-02 16:08

import dezi.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('price', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=dezi.models.filepath)),
            ],
        ),
    ]
