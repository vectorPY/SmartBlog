# Generated by Django 3.0.7 on 2020-07-01 13:23

import comments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=115)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=1800, validators=[comments.models.validate_content])),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]