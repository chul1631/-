# Generated by Django 3.2.13 on 2022-12-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petplace',
            name='url',
            field=models.TextField(),
        ),
    ]
