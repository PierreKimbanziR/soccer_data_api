from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


from rest_framework import status
from season_stats.models import TeamSeasonStats
from season_stats.serializers import TeamSeasonStatsSerializer
from season_stats.models import PlayerSeasonStats
from season_stats.serializers import PlayerSeasonStatsSerializer
from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter

from rest_framework import permissions
from season_stats import custompermissions

from rest_framework.throttling import ScopedRateThrottle


class TeamSeasonStatsList(generics.ListCreateAPIView):
    queryset = TeamSeasonStats.objects.all()
    serializer_class = TeamSeasonStatsSerializer
    name = "teams-season-stats-list"
    filter_fields = ("team_name",)
    search_fields = ("^team_name",)
    ordering_fields = ("team_name",)
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermissions.IsCurrentUserOwnerOrReadOnly,
    )
    throttle_scope = "teams"
    throttle_classes = (ScopedRateThrottle,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TeamSeasonStatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamSeasonStats.objects.all()
    serializer_class = TeamSeasonStatsSerializer
    name = "teams-season-stats-detail"
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermissions.IsCurrentUserOwnerOrReadOnly,
    )
    throttle_scope = "teams"
    throttle_classes = (ScopedRateThrottle,)


class PlayerSeasonsStatsList(generics.ListCreateAPIView):
    queryset = PlayerSeasonStats.objects.all()
    serializer_class = PlayerSeasonStatsSerializer
    name = "players-season-stats-list"
    filter_fields = ("player_name", "team_name")
    ordering_fields = "player_name"
    search_fields = ("player_name",)
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermissions.IsCurrentUserOwnerOrReadOnly,
    )
    throttle_scope = "players"
    throttle_classes = (ScopedRateThrottle,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlayerSeasonStatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerSeasonStats.objects.all()
    serializer_class = PlayerSeasonStatsSerializer
    name = "players-season-stats-detail"
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermissions.IsCurrentUserOwnerOrReadOnly,
    )
    throttle_scope = "players"
    throttle_classes = (ScopedRateThrottle,)


class SeasonStatsRoot(generics.GenericAPIView):
    name = "season-stats-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "teams": reverse(TeamSeasonStatsList.name, request=request),
                "player": reverse(PlayerSeasonsStatsList.name, request=request),
            }
        )
