# Generated by Django 5.0.1 on 2024-01-31 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendations', models.TextField()),
            ],
        ),
    ]
