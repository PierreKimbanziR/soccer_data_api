# Generated by Django 3.2.5 on 2021-08-04 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_rename_team_season_stats_teamseasonstats'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerseasonstats',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='teams.teamseasonstats'),
        ),
    ]
