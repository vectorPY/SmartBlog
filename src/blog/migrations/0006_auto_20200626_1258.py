# Generated by Django 3.0.7 on 2020-06-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200626_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
