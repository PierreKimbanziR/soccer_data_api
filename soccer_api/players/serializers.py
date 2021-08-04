from soccer_api.teams.models import TeamSeasonStats
from rest_framework import serializers
from models import PlayerSeasonStats
from team.models import TeamSeasonStats

import players.views


class PlayerSeasonStatsSerializer(serializers.HyperlinkedModelSerializer):
    team_name = serializers.SlugRelatedField(
        queryset=TeamSeasonStats.objects.all(), slugfield="team_name"
    )

    class Meta:
        model = PlayerSeasonStats
        fields = "__all__"
