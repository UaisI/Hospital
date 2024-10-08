# Generated by Django 5.1 on 2024-08-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('experience_years', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=40)),
            ],
        ),
    ]
