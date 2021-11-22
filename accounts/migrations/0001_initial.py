# Generated by Django 3.2.9 on 2021-11-21 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='reset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newPassword', models.CharField(max_length=100)),
                ('verify_code', models.CharField(max_length=6)),
            ],
        ),
    ]
