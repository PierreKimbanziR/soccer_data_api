from rest_framework import serializers
from season_stats.models import PlayerSeasonStats, TeamSeasonStats
from django.contrib.auth.models import User


class UserTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSeasonStats
        fields = "team_name"


class UserPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSeasonStats
        fields = "player_name"


class UserSerializer(serializers.ModelSerializer):
    teams = UserTeamSerializer(many=True, read_only=True)
    players = UserPlayerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("pk", "username", "drone", "player")


class TeamSeasonStatsSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True)
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = TeamSeasonStats
        fields = "__all__"


class PlayerSeasonStatsSerializer(serializers.ModelSerializer):
    team_name = serializers.SlugRelatedField(
        queryset=TeamSeasonStats.objects.all(), slug_field="team_name"
    )
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = PlayerSeasonStats
        fields = "__all__"
