# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ano',
            fields=[
                ('identi', models.CharField(max_length=6, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masculino', models.IntegerField(default=0)),
                ('femenino', models.IntegerField(default=0)),
                ('ano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datashow.Ano')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('nombreenf', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('nombremes', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='enfermedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datashow.Enfermedad'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='mes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datashow.Mes'),
        ),
    ]