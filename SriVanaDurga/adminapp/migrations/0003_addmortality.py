# Generated by Django 5.0 on 2024-03-22 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_rename_addchickstable_addchicks'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddMortality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('cause_of_death', models.CharField(choices=[('disease', 'Disease'), ('accident', 'Accident'), ('other', 'Other')], max_length=50)),
                ('notes', models.CharField(blank=True, null=True)),
            ],
            options={
                'db_table': 'addmortality_table',
            },
        ),
    ]
