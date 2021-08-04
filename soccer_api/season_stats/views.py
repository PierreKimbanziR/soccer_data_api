from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


from rest_framework import status
from season_stats.models import TeamSeasonStats
from season_stats.serializers import TeamSeasonStatsSerializer
from season_stats.models import PlayerSeasonStats
from season_stats.serializers import PlayerSeasonStatsSerializer


class TeamSeasonStatsList(generics.ListAPIView):
    queryset = TeamSeasonStats.objects.all()
    serializer_class = TeamSeasonStatsSerializer
    name = "team-season-stats-list"


class TeamSeasonStatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamSeasonStats.objects.all()
    serializer_class = TeamSeasonStatsSerializer
    name = "team-season-stats-detail"


class PlayerSeasonsStatsList(generics.ListAPIView):
    queryset = PlayerSeasonStats.objects.all()
    serializer_class = PlayerSeasonStatsSerializer
    name = "player-stats-list"


class PlayerSeasonStatsDetail(generics.RetrieveUpdateAPIView):
    queryset = PlayerSeasonStats.objects.all()
    serializer_class = PlayerSeasonStatsSerializer
    name = "player-stats-detail"
