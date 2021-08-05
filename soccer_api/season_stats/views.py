from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


from rest_framework import status
from season_stats.models import TeamSeasonStats
from season_stats.serializers import TeamSeasonStatsSerializer
from season_stats.models import PlayerSeasonStats
from season_stats.serializers import PlayerSeasonStatsSerializer


class TeamSeasonStatsList(generics.ListCreateAPIView):
    queryset = TeamSeasonStats.objects.all()
    serializer_class = TeamSeasonStatsSerializer
    name = "teams-season-stats-list"


class TeamSeasonStatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamSeasonStats.objects.all()
    serializer_class = TeamSeasonStatsSerializer
    name = "teams-season-stats-detail"


class PlayerSeasonsStatsList(generics.ListCreateAPIView):
    queryset = PlayerSeasonStats.objects.all()
    serializer_class = PlayerSeasonStatsSerializer
    name = "players-season-stats-list"


class PlayerSeasonStatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerSeasonStats.objects.all()
    serializer_class = PlayerSeasonStatsSerializer
    name = "players-season-stats-detail"


class SeasonStatsRoot(generics.GenericAPIView):
    name = "season-stats-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "teams": reverse(TeamSeasonStatsList.name, request=request),
                "player": reverse(PlayerSeasonsStatsList.name, request=request),
            }
        )
