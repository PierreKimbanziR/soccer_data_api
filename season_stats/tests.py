from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from season_stats.models import PlayerSeasonStats, TeamSeasonStats
from faker import Faker
from season_stats import views
from django.contrib.auth.models import User


class TeamsSeasonStatsTests(APITestCase):
    
    def create_user(self):
        fk = Faker()
        username = fk.first_name()+fk.last_name()
        email = f'{username}@gmail.com'
        password = "testtest1234"
        user = User.objects.create_user(username, email, password)
        self.client.login(username=username, password=password)

    def post_team_stat(self, team_name):
        url = reverse(views.TeamSeasonStatsList.name)
        data = {
            "team_name": team_name,
            "players": [],
            "number_of_players": 0,
            "mean_age_of_players": 0,
            "possession": 48.6,
            "matches_played": 38,
            "starts": 38,
            "minutes_played": 366,
            "minutes_played_by_90": 346.9,
            "goals_scored": 33,
            "assists": 33,
            "non_penalty_goals": 4,
            "penalty_goals": 4,
            "penalty_attempted": 3,
            "yellow_cards": 3,
            "red_cards": 3,
            "goals_per_90": 3.8,
            "assists_per_90": 3.9,
            "gls_asts_per_90": 3.0,
            "non_penalty_goals_per_90": 3.0,
            "non_penalty_goals_ast_per_90": 7.9,
            "xG": 3.0,
            "npxG": 3.0,
            "xA": 78.0,
            "npxG_xA": 3.0,
            "xG_per_90": 3.0,
            "xA_per_90": 78.0,
            "xG_xA_per_90": 78.0,
            "npxG_per_90": 78.0,
            "npxG_xA_per_90": 78.0,
        }
        self.create_user()
        response = self.client.post(url, data, format="json")
        return response

    def test_post_team_name(self):
        team_name = "FCpierre"

        response = self.post_team_stat(team_name)
        assert response.status_code == status.HTTP_201_CREATED

    def test_post_and_get_single_team_season_stats(self):
        """
        Ensure we create new teams_stats instance and then retrieve it
        """
        new_team_name = "Fc Soignies"
        response = self.post_team_stat(new_team_name)
        self.client.login(username="pierre", password="test")
        print("Pk {0}".format(TeamSeasonStats.objects.get().team_name))
        assert response.status_code == status.HTTP_201_CREATED
        assert TeamSeasonStats.objects.count() == 1
        assert TeamSeasonStats.objects.get().team_name == new_team_name

    def test_post_existing_team_name(self):
        """
        Ensure we cannot create mutiple teams with the same name
        """
        new_team_name = "FC bggggg"
        response1 = self.post_team_stat(new_team_name)
        assert response1.status_code == status.HTTP_201_CREATED
        
        response2 = self.post_team_stat(new_team_name)
        assert response2.status_code == status.HTTP_400_BAD_REQUEST

    def test_filtering_team_name(self):
        """
        Ensure we can filter team by team_name
        """
        team_name1 = "FC beauxgosses"
        team_name2 = "FC chaoros"
        self.post_team_stat(team_name1)
        self.post_team_stat(team_name2)
        filter_by_name = {"team_name": team_name1}
        url = "{0}?{1}".format(
            reverse(views.TeamSeasonStatsList.name), urlencode(filter_by_name)
        )
        print(url)
        response = self.client.get(url, format="json")
        print(response)
        assert response.status_code == status.HTTP_200_OK
        # Make sure we receive  only one element in the response
        assert response.data["count"] == 1
        assert response.data["results"][0]["team_name"] == team_name1

    def test_retrieving_teams_collection(self):
        new_team_name = "Grabuge RFC"
        self.post_team_stat(new_team_name)
        url = reverse(views.TeamSeasonStatsList.name)
        response = self.client.get(
            url,
            format="json",
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["team_name"] == new_team_name

    def test_update_team_data(self):
        new_team_name = "AC Bagarre"
        response = self.post_team_stat(new_team_name)
        url = reverse(
            views.TeamSeasonStatsDetail.name, args={response.data["team_name"]}
        )
        print(url)
        updated_team_name = "AC bagarre222"
        data = {
            "team_name": updated_team_name,
            "players": [],
            "number_of_players": 0,
            "mean_age_of_players": 0,
            "possession": 48.6,
            "matches_played": 38,
            "starts": 38,
            "minutes_played": 366,
            "minutes_played_by_90": 346.9,
            "goals_scored": 33,
            "assists": 33,
            "non_penalty_goals": 4,
            "penalty_goals": 4,
            "penalty_attempted": 3,
            "yellow_cards": 3,
            "red_cards": 3,
            "goals_per_90": 3.8,
            "assists_per_90": 3.9,
            "gls_asts_per_90": 3.0,
            "non_penalty_goals_per_90": 3.0,
            "non_penalty_goals_ast_per_90": 7.9,
            "xG": 3.0,
            "npxG": 3.0,
            "xA": 78.0,
            "npxG_xA": 3.0,
            "xG_per_90": 3.0,
            "xA_per_90": 78.0,
            "xG_xA_per_90": 78.0,
            "npxG_per_90": 78.0,
            "npxG_xA_per_90": 78.0,
        }
        patch_response = self.client.patch(url, data, format="json")
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data["team_name"] == updated_team_name

    def test_get_team_by_name(self):
        new_team_name = "FC Tagada"
        response = self.post_team_stat(new_team_name)
        url = reverse(
            views.TeamSeasonStatsDetail.name, None, {response.data["team_name"]}
        )
        get_response = self.client.get(url, format="json")
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data["team_name"] == new_team_name

class PlayerSeasonStatsTests(APITestCase):
    
    def create_user(self):
        fk = Faker()
        username = fk.first_name()+fk.last_name()
        email = f'{username}@gmail.com'
        password = "testtest1234"
        user = User.objects.create_user(username, email, password)
        self.client.login(username=username, password=password)

    def post_player_stats(self, player_name):
        url = reverse(views.PlayerSeasonsStatsList.name)
        data = {
            "player_name": player_name,
            "team_name": "",
            "nation": "ar ARG",
            "position": "GK",
            "age": 27,
            "matches_played": 38,
            "starts": 38,
            "minutes_played": 3420,
            "minutes_played_by_90": 38.0,
            "goals_scored": 0,
            "assists": 0,
            "non_penalty_goals": 0,
            "penalty_goals": 0,
            "penalty_attempted": 0,
            "yellow_cards": 1,
            "red_cards": 0,
            "goals_per_90": 0.0,
            "assists_per_90": 0.0,
            "gls_asts_per_90": 0.0,
            "non_penalty_goals_per_90": 0.0,
            "non_penalty_goals_ast_per_90": 0.0,
            "xG": 0.0,
            "npxG": 0.0,
            "xA": 0.2,
            "npxG_xA": 0.2,
            "xG_per_90": 0.0,
            "xA_per_90": 0.01,
            "xG_xA_per_90": 0.01,
            "npxG_per_90": 0.0,
            "npxG_xA_per_90": 0.01
        }
        self.create_user()
        response = self.client.post(url, data, format="json")
        return response

    def test_post_player(self):
        team_name = "FCpierre"
        response = self.post_player_stats(team_name)
        assert response.status_code == status.HTTP_201_CREATED

    def test_post_and_get_single_player_stats(self):
        """
        Ensure we create new player_stats instance and then retrieve it
        """
        player_name = "Jean_Luc_Duduche"
        response = self.post_player_stats(player_name)
        print("Pk {0}".format(PlayerSeasonStats.objects.get().team_name))
        assert response.status_code == status.HTTP_201_CREATED
        assert PlayerSeasonStats.objects.count() == 1
        assert PlayerSeasonStats.objects.get().player_name == player_name

    def test_post_existing_team_name(self):
        """
        Ensure we cannot create mutiple teams with the same name
        """
        player_name = "axel_foley"
        response1 = self.post_player_stats(player_name)
        assert response1.status_code == status.HTTP_201_CREATED
        
        response2 = self.post_player_stats(player_name)
        assert response2.status_code == status.HTTP_400_BAD_REQUEST

    def test_filtering_team_name(self):
        """
        Ensure we can filter team by team_name
        """
        player_name1 = "Freacois_Venant"
        player_name2 = "Jean_Tand"
        self.post_player_stats(player_name1)
        self.post_player_stats(player_name2)
        filter_by_name = {"player_name": player_name1}
        url = "{0}?{1}".format(
            reverse(views.PlayerSeasonsStatsList.name), urlencode(filter_by_name)
        )
        print(url)
        response = self.client.get(url, format="json")
        print(response)
        assert response.status_code == status.HTTP_200_OK
        # Make sure we receive  only one element in the response
        assert response.data["count"] == 1
        assert response.data["results"][0]["player_name"] == player_name1

    def test_retrieving_teams_collection(self):
        player_name = "Gregory_Lebel"
        self.post_player_stats(player_name)
        url = reverse(views.PlayerSeasonsStatsList.name)
        response = self.client.get(
            url,
            format="json",
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["player_name"] == player_name

    def test_update_team_data(self):
        player_name = "Cristiano_Ronaldo"
        response = self.post_player_stats(player_name)
        url = reverse(
            views.PlayerSeasonStatsDetail.name, args={response.data["player_name"]}
        )
        print(url)
        updated_player_name = "Cristiano_Ronaldo_Jr"
        data = {
            "player_name": updated_player_name,
            "team_name": "",
            "nation": "ar ARG",
            "position": "GK",
            "age": 27,
            "matches_played": 38,
            "starts": 38,
            "minutes_played": 3420,
            "minutes_played_by_90": 38.0,
            "goals_scored": 0,
            "assists": 0,
            "non_penalty_goals": 0,
            "penalty_goals": 0,
            "penalty_attempted": 0,
            "yellow_cards": 1,
            "red_cards": 0,
            "goals_per_90": 0.0,
            "assists_per_90": 0.0,
            "gls_asts_per_90": 0.0,
            "non_penalty_goals_per_90": 0.0,
            "non_penalty_goals_ast_per_90": 0.0,
            "xG": 0.0,
            "npxG": 0.0,
            "xA": 0.2,
            "npxG_xA": 0.2,
            "xG_per_90": 0.0,
            "xA_per_90": 0.01,
            "xG_xA_per_90": 0.01,
            "npxG_per_90": 0.0,
            "npxG_xA_per_90": 0.01
        }
        patch_response = self.client.patch(url, data, format="json")
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data["player_name"] == updated_player_name

    def test_get_team_by_name(self):
        player_name = "Frederic_Lemaitre"
        response = self.post_player_stats(player_name)
        url = reverse(
            views.PlayerSeasonStatsDetail.name, None, {response.data["player_name"]}
        )
        get_response = self.client.get(url, format="json")
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data["player_name"] == player_name
# Create your tests here.
