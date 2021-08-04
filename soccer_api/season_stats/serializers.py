from soccer_api.teams.models import TeamSeasonStats
from rest_framework import serializers
from .models import PlayerSeasonStats, TeamSeasonStats




class TeamSeasonStatsSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="player-stats-detail"
    )

    class Meta:
        model = TeamSeasonStats
        fields = "__all__"


class PlayerSeasonStatsSerializer(serializers.HyperlinkedModelSerializer):
    team_name = serializers.SlugRelatedField(
        queryset=TeamSeasonStats.objects.all(), slugfield="team_name"
    )

    class Meta:
        model = PlayerSeasonStats
        fields = "__all__"
