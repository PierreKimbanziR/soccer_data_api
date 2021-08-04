# Create your models here.
from django.db import models
from django.db.models.lookups import StartsWith

# Create your models here.
class PlayerSeasonStats(models.Model):

    team_name = models.ForeignKey(
        "teams.TeamSeasonStats", on_delete=models.CASCADE, related_name="players"
    )

    player_name = models.CharField(max_length=200, primary_key=True)
    nation = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    age = models.IntegerField()
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
        return self.player_name

    def save(self, *args, **kwargs):
        self.full_clean()
        super(PlayerSeasonStats, self).save(*args, **kwargs)

    def clean(self):
        if self.player_name:
            self.player_name = self.player_name.strip()

    class Meta:
        ordering = ("player_name",)
