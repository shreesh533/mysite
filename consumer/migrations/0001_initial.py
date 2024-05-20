# Generated by Django 5.0.6 on 2024-05-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'indexes': [models.Index(fields=['phone'], name='consumer_us_phone_b6d49e_idx')],
            },
        ),
    ]
