# Generated by Django 3.0.7 on 2020-07-21 17:07

from django.db import migrations, models
import ideas.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=115)),
                ('subject', models.CharField(max_length=115, validators=[ideas.models.validate])),
                ('content', models.CharField(max_length=1500, validators=[ideas.models.validate])),
                ('reviewed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
