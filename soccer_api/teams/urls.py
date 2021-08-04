from django.conf.urls import url
from teams import views

urlpatterns = [
    url(r"^season_stats/$", views.teams_stat_list),
    url(r"^season_stats/(?P<team_name>[\w\s]+)/$", views.team_detail),
]
