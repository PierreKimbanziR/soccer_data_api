from rest_framework import serializers
from .models import TeamSeasonStats


class TeamSeasonStatsSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="player-stats-detail"
    )

    class Meta:
        model = TeamSeasonStats
        fields = "__all__"
