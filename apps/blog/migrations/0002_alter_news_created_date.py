# Generated by Django 4.2.7 on 2023-12-14 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
