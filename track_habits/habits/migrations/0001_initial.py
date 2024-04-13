# Generated by Django 5.0.4 on 2024-04-10 12:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('place', models.CharField(max_length=200, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=200, verbose_name='действие')),
                ('is_pleasure', models.BooleanField(default=True, verbose_name='признак приятной привычки')),
                ('periodic', models.IntegerField(default=1, verbose_name='периодичность в днях')),
                ('award', models.CharField(blank=True, max_length=150, null=True, verbose_name='вознаграждение')),
                ('time_exec', models.TimeField(blank=True, default='00:02', null=True, verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=True, verbose_name='признак публичности')),
                ('associated_habits', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='habits_associated', to='habits.habit', verbose_name='связанная привычка')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='создатель')),
            ],
        ),
    ]