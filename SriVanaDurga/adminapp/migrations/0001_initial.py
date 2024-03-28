# Generated by Django 5.0 on 2024-03-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddChicksTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('birds', models.IntegerField()),
                ('weeks', models.IntegerField()),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'addchicks_table',
            },
        ),
    ]
