from rest_framework import serializers
from .models import TeamSeasonStats


class TeamSeasonStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSeasonStats
        fields = "__all__"
