# Generated by Django 4.1.3 on 2022-11-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('rank', models.IntegerField()),
                ('point', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
