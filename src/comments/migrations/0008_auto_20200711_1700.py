# Generated by Django 3.0.7 on 2020-07-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_auto_20200708_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcomment',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]