# Generated by Django 3.0.7 on 2020-07-04 14:58

import comments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_by', models.CharField(max_length=115)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('reason', models.CharField(max_length=415, validators=[comments.models.validate_reason])),
            ],
        ),
    ]
