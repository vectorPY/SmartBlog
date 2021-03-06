# Generated by Django 3.0.7 on 2020-07-14 18:03

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banned_by', models.CharField(max_length=115)),
                ('user', models.CharField(max_length=115)),
                ('reason', models.CharField(max_length=415, validators=[accounts.models.validate_reason])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
