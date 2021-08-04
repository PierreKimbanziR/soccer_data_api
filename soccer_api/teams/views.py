from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from teams.models import TeamSeasonStats
from teams.serializers import TeamSeasonStatsSerializer


@api_view(["GET", "POST"])
def teams_stat_list(request):
    print("list function")
    if request.method == "GET":
        teams = TeamSeasonStats.objects.all()
        team_serializer = TeamSeasonStatsSerializer(teams, many=True)
        return Response(team_serializer.data)

    elif request.method == "POST":
        teams_serializer = TeamSeasonStatsSerializer(data=request.data)
        if teams_serializer.is_valid():
            teams_serializer.save()
            return Response(teams_serializer.data, status=status.HTTP_201_CREATED)
        return Response(teams_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def team_detail(request, team_name):

    try:
        team = TeamSeasonStats.objects.get(team_name=team_name)
    except TeamSeasonStats.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        team_serializer = TeamSeasonStatsSerializer(team)
        return Response(team_serializer.data)

    elif request.method == "PUT":

        teams_serializer = TeamSeasonStatsSerializer(request.data)
        if teams_serializer.is_valid():
            teams_serializer.save()
            return Response(teams_serializer.data, status=status.HTTP_201_CREATED)

        return Response(teams_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
