# Generated by Django 3.0.3 on 2020-02-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='observation',
            field=models.TextField(blank=True),
        ),
    ]
