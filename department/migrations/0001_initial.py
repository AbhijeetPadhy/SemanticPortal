# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 02:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Professor_file', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester', models.CharField(max_length=3)),
                ('Result_file', models.FileField(upload_to=b'')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start', models.IntegerField(max_length=4)),
                ('End', models.IntegerField(max_length=4)),
                ('Student_file', models.FileField(upload_to=b'')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='Session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Session'),
        ),
    ]
