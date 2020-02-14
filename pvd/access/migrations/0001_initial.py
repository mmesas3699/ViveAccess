# Generated by Django 3.0.3 on 2020-02-11 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('document', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name_1', models.CharField(max_length=80)),
                ('last_name_2', models.CharField(max_length=80)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='students', to='access.Grade')),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('name', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computers', to='access.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('entry', models.TimeField(auto_now=True)),
                ('departure', models.TimeField(null=True)),
                ('observation', models.TextField()),
                ('accessory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='access', to='access.Accessory')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='access', to='access.Computer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access', to='access.Student')),
            ],
        ),
    ]