from django.conf.urls import url
from season_stats import views

urlpatterns = [
    url(
        r"^teams/$",
        views.TeamSeasonStatsList.as_view(),
        name=views.TeamSeasonStatsList.name,
    ),
    url(
        r"^teams/(?P<pk>[\w\s]+)$",
        views.TeamSeasonStatsDetail.as_view(),
        name=views.TeamSeasonStatsDetail.name,
    ),
    url(
        r"^players/$",
        views.PlayerSeasonsStatsList.as_view(),
        name=views.PlayerSeasonsStatsList.name,
    ),
    url(
        r"^players/(?P<pk>[-\w\s]+)$",
        views.PlayerSeasonStatsDetail.as_view(),
        name=views.PlayerSeasonStatsDetail.name,
    ),
    url(r"^$", views.SeasonStatsRoot.as_view(), name=views.SeasonStatsRoot.name),
]
