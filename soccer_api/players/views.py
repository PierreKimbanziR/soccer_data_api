from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from players.models import PlayerSeasonStats
from players.serializers import PlayerSeasonStatsSerializer


class PlayerSeasonsStatsList(generics.ListAPIView):
    queryset = PlayerSeasonStats.objects.all()
    serializer_class = PlayerSeasonStatsSerializer
    name = "player-stats-list"

class PlayerSeasonStatsDetail(generics.RetrieveUpdateAPIView):
    queryset = PlayerSeasonStats.objects.all()
    serializer_class = PlayerSeasonStatsSerializer
    name = "player-stats-detail"

