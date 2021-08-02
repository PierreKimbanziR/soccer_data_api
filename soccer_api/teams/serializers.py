from rest_framework import serializers
from .models import TeamSeasonStats


class TeamSeasonStatsSerializer(serializers.ModelSerializer):
    model: TeamSeasonStats
    fields: "__all__"
