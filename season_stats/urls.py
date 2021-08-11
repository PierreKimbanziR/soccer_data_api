from django.urls import re_path
from season_stats import views

urlpatterns = [
    re_path(
        r"^teams/$",
        views.TeamSeasonStatsList.as_view(),
        name=views.TeamSeasonStatsList.name,
    ),
    re_path(
        r"^teams/(?P<pk>[\w\s]+)$",
        views.TeamSeasonStatsDetail.as_view(),
        name=views.TeamSeasonStatsDetail.name,
    ),
    re_path(
        r"^players/$",
        views.PlayerSeasonsStatsList.as_view(),
        name=views.PlayerSeasonsStatsList.name,
    ),
    re_path(
        r"^players/(?P<pk>[-\w\s]+)$",
        views.PlayerSeasonStatsDetail.as_view(),
        name=views.PlayerSeasonStatsDetail.name,
    ),
    re_path(r"^$", views.SeasonStatsRoot.as_view(), name=views.SeasonStatsRoot.name),
]
