# Generated by Django 3.2 on 2021-04-19 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Name', models.CharField(max_length=50)),
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('EmailID', models.EmailField(max_length=50)),
                ('Address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
