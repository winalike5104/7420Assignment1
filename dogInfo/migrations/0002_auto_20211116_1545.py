# Generated by Django 3.2.9 on 2021-11-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='birthday',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
