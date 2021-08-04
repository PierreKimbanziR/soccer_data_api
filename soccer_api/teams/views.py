from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


from rest_framework import status
from teams.models import TeamSeasonStats
from teams.serializers import TeamSeasonStatsSerializer


class TeamSeasonStatsList(generics.ListAPIView):
    queryset = TeamSeasonStats.objects.all()
    serializer_class = TeamSeasonStatsSerializer
    name = "team-season-stats-list"


class TeamSeasonStatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamSeasonStats.objects.all()
    serializer_class = TeamSeasonStatsSerializer
    name = "team-season-stats-detai"
