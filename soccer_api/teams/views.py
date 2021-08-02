from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from teams.models import TeamSeasonStats
from teams.serializers import TeamSeasonStatsSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs["content_type"] = "application/json"
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def teams_stat_list(request):
    if request.method == "GET":
        teams = TeamSeasonStats.objects.all()
        team_serializer = TeamSeasonStatsSerializer(teams, many=True)
        return JSONResponse(team_serializer.data)
    elif request.method == "POST":
        teams_data = JSONParser().parse(request)
        teams_serializer = TeamSeasonStatsSerializer(data=teams_data)
        if teams_serializer.is_valid():
            teams_serializer.save()
            return JSONResponse(teams_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(teams_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def team_detail(request, team_name):
    try:
        team = TeamSeasonStats.objects.get(team_name=team_name)
    except TeamSeasonStats.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        team_serializer = TeamSeasonStatsSerializer(team)
        return JSONResponse(team_serializer.data)
    elif request.method == "PUT":
        team_data = JSONParser().parse(request)
        teams_serializer = TeamSeasonStatsSerializer(team_data)
        if teams_serializer.is_valid():
            teams_serializer.save()
            return JSONResponse(teams_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(teams_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        team.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
