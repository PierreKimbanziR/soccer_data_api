from django.db import models
from django.db.models.lookups import StartsWith

# Create your models here.
class TeamSeasonStats(models.Model):
    team_name = models.CharField(max_length=200, primary_key=True)
    owner = models.ForeignKey(
        "auth.User",
        related_name="teams",
        on_delete=models.CASCADE,
    )
    number_of_players = models.IntegerField()
    mean_age_of_players = models.FloatField()
    possession = models.FloatField()
    matches_played = models.IntegerField()
    starts = models.IntegerField()
    minutes_played = models.IntegerField()
    minutes_played_by_90 = models.FloatField()

    goals_scored = models.IntegerField()
    assists = models.IntegerField()
    non_penalty_goals = models.IntegerField()
    penalty_goals = models.IntegerField()
    penalty_attempted = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    goals_per_90 = models.FloatField()
    assists_per_90 = models.FloatField()
    gls_asts_per_90 = models.FloatField()
    non_penalty_goals_per_90 = models.FloatField()
    non_penalty_goals_ast_per_90 = models.FloatField()

    xG = models.FloatField()
    npxG = models.FloatField()
    xA = models.FloatField()
    npxG_xA = models.FloatField()

    xG_per_90 = models.FloatField()
    xA_per_90 = models.FloatField()
    xG_xA_per_90 = models.FloatField()
    npxG_per_90 = models.FloatField()
    npxG_xA_per_90 = models.FloatField()

    def __str__(self):
        return self.team_name

    class Meta:
        ordering = ("team_name",)


# Create your models here.
class PlayerSeasonStats(models.Model):

    team_name = models.ForeignKey(
        "TeamSeasonStats",
        on_delete=models.CASCADE,
        related_name="players",
        blank=True,
        null=True,
    )

    player_name = models.CharField(
        max_length=200,
        primary_key=True,
    )
    owner = models.ForeignKey("auth.User", related_name="+", on_delete=models.CASCADE)
    nation = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    age = models.IntegerField()
    matches_played = models.IntegerField()
    starts = models.IntegerField()
    minutes_played = models.IntegerField()
    minutes_played_by_90 = models.FloatField()

    goals_scored = models.IntegerField()
    assists = models.IntegerField()
    non_penalty_goals = models.IntegerField()
    penalty_goals = models.IntegerField()
    penalty_attempted = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    goals_per_90 = models.FloatField()
    assists_per_90 = models.FloatField()
    gls_asts_per_90 = models.FloatField()
    non_penalty_goals_per_90 = models.FloatField()
    non_penalty_goals_ast_per_90 = models.FloatField()

    xG = models.FloatField()
    npxG = models.FloatField()
    xA = models.FloatField()
    npxG_xA = models.FloatField()

    xG_per_90 = models.FloatField()
    xA_per_90 = models.FloatField()
    xG_xA_per_90 = models.FloatField()
    npxG_per_90 = models.FloatField()
    npxG_xA_per_90 = models.FloatField()

    def __str__(self):
        return self.player_name

    def create_player_name(self):
        return f"{self.first_name}_{self.last_name}"

    class Meta:
        ordering = ("player_name",)
