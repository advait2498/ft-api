# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-26 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ft_api', '0002_auto_20180126_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'exercise',
            },
        ),
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('multiplier', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'exercise_type',
            },
        ),
        migrations.CreateModel(
            name='FitnessPlan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goal_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fitness_plan',
            },
        ),
        migrations.CreateModel(
            name='FitnessPlanType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('pounds_per_week', models.DecimalField(decimal_places=2, max_digits=5)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'fitness_plan_type',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='fitnessplan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='ft_api.User'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='exercise_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='ft_api.ExerciseType'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='ft_api.User'),
        ),
    ]
