# Generated by Django 3.2.5 on 2021-08-05 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('number_of_players', models.IntegerField()),
                ('mean_age_of_players', models.FloatField()),
                ('possession', models.FloatField()),
                ('matches_played', models.IntegerField()),
                ('starts', models.IntegerField()),
                ('minutes_played', models.IntegerField()),
                ('minutes_played_by_90', models.FloatField()),
                ('goals_scored', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('non_penalty_goals', models.IntegerField()),
                ('penalty_goals', models.IntegerField()),
                ('penalty_attempted', models.IntegerField()),
                ('yellow_cards', models.IntegerField()),
                ('red_cards', models.IntegerField()),
                ('goals_per_90', models.FloatField()),
                ('assists_per_90', models.FloatField()),
                ('gls_asts_per_90', models.FloatField()),
                ('non_penalty_goals_per_90', models.FloatField()),
                ('non_penalty_goals_ast_per_90', models.FloatField()),
                ('xG', models.FloatField()),
                ('npxG', models.FloatField()),
                ('xA', models.FloatField()),
                ('npxG_xA', models.FloatField()),
                ('xG_per_90', models.FloatField()),
                ('xA_per_90', models.FloatField()),
                ('xG_xA_per_90', models.FloatField()),
                ('npxG_per_90', models.FloatField()),
                ('npxG_xA_per_90', models.FloatField()),
            ],
            options={
                'ordering': ('team_name',),
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('nation', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('matches_played', models.IntegerField()),
                ('starts', models.IntegerField()),
                ('minutes_played', models.IntegerField()),
                ('minutes_played_by_90', models.FloatField()),
                ('goals_scored', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('non_penalty_goals', models.IntegerField()),
                ('penalty_goals', models.IntegerField()),
                ('penalty_attempted', models.IntegerField()),
                ('yellow_cards', models.IntegerField()),
                ('red_cards', models.IntegerField()),
                ('goals_per_90', models.FloatField()),
                ('assists_per_90', models.FloatField()),
                ('gls_asts_per_90', models.FloatField()),
                ('non_penalty_goals_per_90', models.FloatField()),
                ('non_penalty_goals_ast_per_90', models.FloatField()),
                ('xG', models.FloatField()),
                ('npxG', models.FloatField()),
                ('xA', models.FloatField()),
                ('npxG_xA', models.FloatField()),
                ('xG_per_90', models.FloatField()),
                ('xA_per_90', models.FloatField()),
                ('xG_xA_per_90', models.FloatField()),
                ('npxG_per_90', models.FloatField()),
                ('npxG_xA_per_90', models.FloatField()),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='season_stats.team')),
            ],
            options={
                'ordering': ('player_name',),
            },
        ),
    ]