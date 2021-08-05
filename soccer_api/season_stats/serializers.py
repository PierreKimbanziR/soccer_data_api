from rest_framework import serializers
from season_stats.models import PlayerSeasonStats, TeamSeasonStats


class TeamSeasonStatsSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True)

    class Meta:
        model = TeamSeasonStats
        fields = "__all__"


class PlayerSeasonStatsSerializer(serializers.ModelSerializer):
    team_name = serializers.SlugRelatedField(
        queryset=TeamSeasonStats.objects.all(), slug_field="team_name"
    )

    class Meta:
        model = PlayerSeasonStats
        fields = "__all__"
